"""Parse jupytext-percent notebook exercise files into structured cells.

See templates/notebook_format/FORMAT.md. Shared by convert_exercises.py
(manifest generation) and any tool that needs cell structure.
"""

import re

_MARKER = re.compile(r"^# %%(.*)$", re.M)


def parse_cells(content: str) -> list[dict] | None:
    """Split file content into ordered cells.

    Returns None if the file has no cell markers (not notebook format).
    Each cell: {"type": "markdown"|"code", "locked": bool, "source": str}.
    The header block before the first marker is not a cell.
    """
    matches = list(_MARKER.finditer(content))
    if not matches:
        return None

    cells = []
    for i, m in enumerate(matches):
        kind = m.group(1).strip()
        start = m.end() + 1
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        source = content[start:end].rstrip()
        if kind == "[markdown]":
            # Strip the leading "# " comment prefix from markdown lines
            text = "\n".join(
                ln[2:] if ln.startswith("# ") else ln.lstrip("#")
                for ln in source.split("\n")
            ).strip()
            cells.append({"type": "markdown", "locked": False, "source": text})
        else:
            cells.append({
                "type": "code",
                "locked": kind == "locked",
                "source": source,
            })
    return cells


def code_of(cells: list[dict]) -> str:
    """The student-runnable file: concatenated code cells."""
    return "\n\n".join(
        c["source"] for c in cells if c["type"] == "code" and c["source"].strip()
    )
