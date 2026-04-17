# PNG to ICO Converter

Converts a PNG image to a multi-resolution ICO file (Windows icon format). Usable directly as a CLI script or imported as a library. A GUI is planned for a future release.

---

## Features

- Generates a single ICO containing all standard Windows sizes: 16×16, 32×32, 48×48, 64×64, 128×128, 256×256
- Preserves transparency (RGBA)
- Custom size selection via `--sizes`
- Output folder configurable via `$OUTPUT_FOLDER` env var
- JSON output to stdout — agent-friendly

---

## Requirements

- Python 3.x
- [Pillow](https://pypi.org/project/Pillow/) >= 10.0.0

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Usage

Place your PNG in the `input/` directory, then run:

```bash
python core/converter.py logo.png icon.ico
```

Output is written to `output/icon.ico` by default.

### Custom sizes

```bash
python core/converter.py logo.png icon.ico --sizes 16,32,256
```

### Custom output folder

```bash
export OUTPUT_FOLDER="./my_icons"
python core/converter.py logo.png icon.ico
```

### Input resolution

Bare filenames are looked up inside `input/`; full or relative paths are used as-is:

```bash
# These are equivalent if logo.png is in input/
python core/converter.py logo.png icon.ico
python core/converter.py input/logo.png icon.ico
```

---

## File Structure

```
png_to_ico/
├── main.py                  # Entry point (GUI — not yet implemented)
├── core/
│   ├── __init__.py
│   └── converter.py         # Conversion logic + CLI entry point
├── ui/
│   └── __init__.py          # UI stub
├── requirements.txt
├── AGENT_INSTRUCTIONS.md    # Agent usage guide
└── LICENSE.md
```

---

## Agent Usage

See `AGENT_INSTRUCTIONS.md` for commands, env vars, error handling, and workflows.

---

## Planned

- GUI (PySide6) with drag-and-drop input, size selection, and live preview
- Batch conversion of multiple PNGs in one run

---

## License

LM Stick Non-Commercial License — see [LICENSE.md](LICENSE.md) for full terms.

For commercial use inquiries: `shayaan0303@gmail.com`
