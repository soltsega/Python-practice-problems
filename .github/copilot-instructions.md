**Purpose**
- **Brief:** Guidance for AI coding agents working in this repository: a small Python educational/example workspace organized by topic (data types, control statements, libraries).

**Quick Architecture / Big Picture**
- **What:** A collection of short, runnable Python example scripts grouped by topic under `dataTypes/`, `controlStatements/`, and `libraries/`.
- **Why:** Each file demonstrates language features (e.g., `dataTypes/string.py` shows string methods and an `is_palindrome` helper), so changes should preserve clarity for learners.

**Where to look (key files)**
- `dataTypes/` — examples for core types; see [dataTypes/string.py](dataTypes/string.py) for typical style and examples.
- `controlStatements/` — flow-control examples; see [controlStatements/forLoops.py](controlStatements/forLoops.py).
- `libraries/mathLibraries.py` — library-style utilities intended for reuse.
- `outline.txt` — scope list / potential TODOs; update when adding new topics.

**Concrete Patterns to Follow**
- File-level examples: files are short scripts that run standalone (prints, small helper functions). Prefer small, self-contained examples over large modules.
- Naming: lowercase filenames, words concatenated or with underscores (current files use no underscores often). Keep names descriptive (e.g., `forLoops.py`, `numeric.py`).
- Style: informal, explanatory comments above examples are common — keep or enhance them, don’t remove explanatory text.
- Functions: when adding helpers, define simple top-level functions (see `is_palindrome` in [dataTypes/string.py](dataTypes/string.py)).
- No external deps: the repo currently has no `requirements.txt` or external libraries; avoid adding dependencies without explicit reason.

**Developer Workflows (how to run & test changes)**
- Run any example directly with Python: `python path/to/file.py` (use project's Python interpreter; e.g., Python 3.14 was used in the dev environment).
- There are no automated tests in the repository; validate changes by running modified example scripts and ensuring printed output remains illustrative and correct.

**Change Guidelines for AI Agents**
- Preserve pedagogical clarity: keep examples minimal and well-commented. If you refactor, maintain an easy-to-run example for learners.
- When adding a new topic: add a new file under the appropriate folder, add a short doc comment at the top, and update `outline.txt`.
- Avoid sweeping style-only reformats; keep editing surface-level fixes (typos, clarity) local to the file you change.
- Do not introduce external build or test systems unless the user requests it explicitly.

**Merging/Updating this file**
- If `.github/copilot-instructions.md` already exists, merge by preserving any manual guidance and adding missing repository-specific notes above. Prefer short, actionable additions.

**Examples for common edits (copyable snippets)**
- Add a small helper function preserving style:
```
# in dataTypes/my_example.py
def example_helper(x):
    # short description
    return x * 2

print(example_helper(3))  # demonstrates output
```

**When to interrupt and ask the human**
- If a change requires adding a dependency, CI, or tests, ask before proceeding.
- If an architectural change would convert examples into a package (creating setup files, requirements, or tests), request confirmation.

Please review these instructions and tell me any gaps or local conventions you'd like included (e.g., preferred naming, target Python version, or examples to prioritize).
