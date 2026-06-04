"""Convert legacy exercise .py files to notebook cell format (jupytext-percent).

See templates/notebook_format/FORMAT.md for the target format.

Structure-only conversion: English instruction text moves into markdown cells
verbatim; the Hebrew pass happens separately. Files whose structure defies the
heuristics are copied unconverted and flagged in the report.

Usage:
    python scripts/convert_to_notebook.py            # convert all -> exercises_nb/
    python scripts/convert_to_notebook.py --report   # stats only, write nothing
"""

import ast
import json
import re
import sys
import textwrap
from pathlib import Path

REPO = Path(__file__).parent.parent
SRC_ROOT = REPO / "exercises"
DST_ROOT = REPO / "exercises_nb"

SECTION_EQ = re.compile(r"^# ={10,}\s*$")
SECTION_DASH = re.compile(r"^# --- (.+) ---\s*$")
LOCKED_DOCSTRING = re.compile(r"DO NOT MODIFY|Just read", re.I)
PENCIL = "✏️"


def classify_def(node: ast.FunctionDef, body_lines: list[str]) -> str:
    """locked | editable - based on docstring and pencil markers."""
    doc = ast.get_docstring(node) or ""
    if LOCKED_DOCSTRING.search(doc):
        return "locked"
    return "editable"


def md_cell(lines: list[str]) -> dict:
    return {"type": "markdown", "source": "\n".join(lines).strip()}


def code_cell(source: str, locked: bool = False) -> dict:
    return {"type": "code", "locked": locked, "source": source.rstrip()}


def comment_text(lines: list[str]) -> str:
    """Strip leading '# ' from a run of comment lines."""
    out = []
    for ln in lines:
        s = ln.strip()
        out.append(s[2:] if s.startswith("# ") else s.lstrip("#"))
    return "\n".join(out).strip()


def split_body(node: ast.FunctionDef, lines: list[str]) -> list[dict]:
    """Split a function body into cells at instruction-comment runs.

    A comment run containing the pencil marker becomes a markdown cell;
    code between runs becomes code cells. The def wrapper is dropped and
    the body dedented.
    """
    # Body span starts right after the def line (NOT at body[0].lineno -
    # instruction comments live between the def line and the first statement,
    # which AST does not see). Skip a leading docstring by its line span.
    start = node.lineno  # 0-indexed line after "def ...:"
    if (isinstance(node.body[0], ast.Expr)
            and isinstance(node.body[0].value, ast.Constant)
            and isinstance(node.body[0].value.value, str)):
        start = node.body[0].end_lineno  # skip docstring
    body = textwrap.dedent("\n".join(lines[start:node.end_lineno])).split("\n")

    cells, code_buf, md_buf = [], [], []

    def flush_code():
        src = "\n".join(code_buf).strip("\n")
        if src.strip() and src.strip() != "pass":
            cells.append(code_cell(src))
        code_buf.clear()

    def flush_md():
        if md_buf:
            cells.append(md_cell([comment_text(md_buf)]))
            md_buf.clear()

    i = 0
    while i < len(body):
        ln = body[i]
        if ln.strip().startswith("#"):
            # collect the whole comment run
            run = []
            while i < len(body) and (body[i].strip().startswith("#") or not body[i].strip()):
                run.append(body[i])
                i += 1
            run_text = "\n".join(run)
            # Indented runs sit inside a control block - splitting there would
            # gut the block's body (e.g. a while whose body is comments+pass).
            # Only split at top-level (column 0) pencil runs.
            run_indented = run and run[0] != run[0].lstrip()
            if PENCIL in run_text and not run_indented:
                flush_code()
                flush_md()
                comment_lines = [l for l in run if l.strip().startswith("#")]
                cells.append(md_cell([comment_text(comment_lines)]))
                cells.append(code_cell(f"# {PENCIL} כתבי את הקוד שלך כאן"))
            else:
                code_buf.extend(run)  # ordinary comments stay with code
        else:
            code_buf.append(ln)
            i += 1
    flush_code()
    return cells


def convert_file(path: Path) -> tuple[list[dict], str | None, list[str]]:
    """Returns (cells, header, warnings). Raises on unparseable files."""
    src = path.read_text(encoding="utf-8")
    lines = src.split("\n")
    tree = ast.parse(src)
    warnings = []

    # Header: leading comment block before the docstring
    header_end = 0
    for i, ln in enumerate(lines):
        if ln.startswith('"""') or (ln and not ln.startswith("#")):
            header_end = i
            break
    header = "\n".join(lines[:header_end]).rstrip() or None

    cells: list[dict] = []
    converted_defs: set[str] = set()
    covered_until = header_end  # last source line already consumed

    def consume_gap(upto: int):
        """Comments/sections between AST nodes -> markdown cells."""
        gap = lines[covered_until:upto]
        buf = []
        for ln in gap:
            s = ln.strip()
            if SECTION_EQ.match(s):
                continue
            m = SECTION_DASH.match(s)
            if m:
                if buf:
                    cells.append(md_cell([comment_text(buf)])); buf.clear()
                buf.append(f"# ## {m.group(1)}")
                continue
            if s.startswith("#"):
                buf.append(ln)
            elif not s and buf:
                buf.append("")
        if buf:
            text = comment_text(buf)
            # Section titles from # ==== blocks: single short line -> heading
            if "\n" not in text and text and not text.startswith("##"):
                text = f"## {text}"
            cells.append({"type": "markdown", "source": text})

    for node in tree.body:
        consume_gap(node.lineno - 1)
        if (isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant)
                and isinstance(node.value.value, str)):
            cells.append({"type": "markdown", "source": node.value.value.strip()})
        elif isinstance(node, ast.FunctionDef):
            converted_defs.add(node.name)
            kind = classify_def(node, lines)
            if kind == "locked":
                start = node.lineno  # line after "def ...:" (see split_body)
                if (isinstance(node.body[0], ast.Expr)
                        and isinstance(node.body[0].value, ast.Constant)
                        and isinstance(node.body[0].value.value, str)):
                    start = node.body[0].end_lineno
                body = textwrap.dedent("\n".join(lines[start:node.end_lineno]))
                cells.append(code_cell(body, locked=True))
            else:
                cells.extend(split_body(node, lines))
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            cells.append(code_cell("\n".join(lines[node.lineno - 1:node.end_lineno])))
        elif (isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)
                and isinstance(node.value.func, ast.Name)
                and node.value.func.id in converted_defs):
            pass  # trailing call to a dissolved wrapper - drop
        elif (converted_defs and isinstance(node, ast.Expr)
                and node.lineno > max(n.end_lineno for n in tree.body if isinstance(n, ast.FunctionDef))):
            pass  # driver scaffolding after the last def (banner prints etc.) - dies with the wrappers
        elif isinstance(node, ast.If) and getattr(getattr(node.test, "left", None), "id", "") == "__name__":
            pass  # main guard - drop with the wrappers
        elif isinstance(node, (ast.Assign, ast.AnnAssign, ast.ClassDef, ast.For,
                               ast.While, ast.If, ast.With, ast.Expr)):
            # Top-level data setup, classes (OOP module), or driver code - plain code cell
            cells.append(code_cell("\n".join(lines[node.lineno - 1:node.end_lineno])))
        else:
            warnings.append(f"unhandled top-level node at line {node.lineno}: {type(node).__name__}")
            cells.append(code_cell("\n".join(lines[node.lineno - 1:node.end_lineno])))
        covered_until = node.end_lineno

    consume_gap(len(lines))

    # Merge adjacent markdown cells
    merged: list[dict] = []
    for c in cells:
        if merged and c["type"] == "markdown" and merged[-1]["type"] == "markdown":
            merged[-1]["source"] += "\n\n" + c["source"]
        else:
            merged.append(c)
    return merged, header, warnings


def render(cells: list[dict], header: str | None) -> str:
    out = [header + "\n"] if header else []
    for c in cells:
        if c["type"] == "markdown":
            body = "\n".join(f"# {l}".rstrip() for l in c["source"].split("\n"))
            out.append(f"# %% [markdown]\n{body}\n")
        else:
            marker = "# %% locked" if c.get("locked") else "# %%"
            out.append(f"{marker}\n{c['source']}\n")
    return "\n".join(out)


def main():
    report_only = "--report" in sys.argv
    stats = {"converted": 0, "flagged": 0}
    flagged: dict[str, str] = {}

    for path in sorted(SRC_ROOT.rglob("exercise_*.py")):
        rel = path.relative_to(SRC_ROOT)
        try:
            cells, header, warnings = convert_file(path)
            if warnings:
                flagged[str(rel)] = "; ".join(warnings)
                stats["flagged"] += 1
            stats["converted"] += 1
            if not report_only:
                dst = DST_ROOT / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_text(render(cells, header), encoding="utf-8")
        except Exception as e:
            flagged[str(rel)] = f"FAILED: {type(e).__name__}: {e}"
            stats["flagged"] += 1
            if not report_only:
                dst = DST_ROOT / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")

    print(json.dumps(stats, indent=2))
    if flagged:
        report_path = REPO / "exercises_nb_flagged.json"
        if not report_only:
            report_path.write_text(json.dumps(flagged, indent=2, ensure_ascii=False))
        for f, why in list(flagged.items())[:10]:
            print(f"  FLAG {f}: {why}")
        if len(flagged) > 10:
            print(f"  ... and {len(flagged) - 10} more (see exercises_nb_flagged.json)")


if __name__ == "__main__":
    main()
