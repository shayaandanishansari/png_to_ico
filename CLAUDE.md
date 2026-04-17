# PNG to ICO — Project Brief

## Overview

A tool that converts PNG images to multi-resolution ICO files (Windows icon format). Designed to be used directly via CLI by agents or humans, with a UI layer planned for the future.

---

## Core Features

- Converts PNG → ICO with multiple resolutions in a single file (16×16 through 256×256)
- Preserves transparency (RGBA)
- `$OUTPUT_FOLDER` env var controls output location; defaults to `output/`
- Input resolved from bare filename (looks in `input/`) or full/relative path
- Optional `--sizes` argument to override which resolutions are embedded

---

## File Structure

```
png_to_ico/
├── main.py                  # Entry point (UI stub — not yet implemented)
├── core/
│   ├── __init__.py
│   └── converter.py         # Conversion logic + __main__ CLI block
├── ui/
│   └── __init__.py          # UI stub
├── requirements.txt
├── CLAUDE.md
└── AGENT_INSTRUCTIONS.md
```

**Key design note:** `core/` is UI-agnostic. `converter.py` is both importable as a library and runnable as a CLI script.

---

## Tech Stack

| Component | Library |
|---|---|
| Image processing | [Pillow](https://pypi.org/project/Pillow/) |

---

## Agent-Usable API

`core/converter.py` is directly runnable:

```bash
python core/converter.py logo.png icon.ico
python core/converter.py logo.png icon.ico --sizes 16,32,256
```

See `AGENT_INSTRUCTIONS.md` for full agent usage.

---

## Planned

- GUI (PySide6) with drag-and-drop PNG input, size selection, live preview
- Batch conversion of multiple PNGs in one run
