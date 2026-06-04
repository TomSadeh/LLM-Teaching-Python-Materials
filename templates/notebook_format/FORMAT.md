# Notebook Exercise Format (v1 draft)

Exercises are plain `.py` files in jupytext-percent style: alternating **markdown
cells** (Hebrew narrative, rendered in the UI) and **code cells** (what the
student sees and edits). The student never reads English prose; the runnable
file is the concatenation of code cells only.

## Cell markers

| Marker | Meaning |
|---|---|
| `# %% [markdown]` | Narrative cell. Hebrew text + template variables. Rendered as rich text (RTL) in the UI. Never part of the student's file. |
| `# %%` | Editable code cell. This is where the student writes. |
| `# %% locked` | Read-only code cell (e.g. "read this and predict", spot-the-difference snippets). Shown as code, not editable. |

Everything before the first cell marker is the file header (human-facing
metadata comment block, kept from the legacy format; the sync pipeline reads
metadata from `exercises.json`, not from the header).

## Conversion rules from legacy format

1. Module docstring (`"""{{CONTEXT_*}}..."""`) → first `# %% [markdown]` cell.
2. `# ====` section separators with `{{TITLE}}`/`{{NARRATIVE}}` comments → `# %% [markdown]` cell with `## {{TITLE}}` heading.
3. **Instruction comments inside function bodies move OUT** into the preceding markdown cell, translated to Hebrew. This is the core of the change - the English the student was forced to read lived here.
4. `def exercise_a(): ... pass` wrappers are **dropped**. Cells execute top-to-bottom like Jupyter; each sub-exercise is its own cell with top-level code. (Legacy wrappers forced students in module 0 to stare at `def` syntax that isn't taught until module 5.)
5. `DO NOT MODIFY` functions → `# %% locked` cells with top-level code.
6. ✏️ markers → an editable `# %%` cell, empty except a single Hebrew marker comment.
7. Hints (`# Hint: ...`) → `> רמז: ...` blockquote at the end of the preceding markdown cell. The UI may render these collapsed.
8. Template variables (`{{hero}}`, `{{CONTEXT_*}}`) are preserved verbatim in both cell kinds; resolution stays in the existing theme-variable pipeline.

## Language rules

- Markdown cells: Hebrew, feminine address (matching existing `description_he` convention). Code identifiers, Python keywords, and expected-output literals stay in English/code.
- Code cells: code only. A single `# ✏️ כתבי את הקוד שלך כאן` marker comment is allowed in empty editable cells; no other prose comments.

## What sync stores

`exercises.cells` (JSON): ordered array of `{type: "markdown"|"code", locked: bool, source: str}`.
`starter_code` remains the concatenation of code cells (the runnable file), so
code execution and existing attempt flows keep working unchanged.
