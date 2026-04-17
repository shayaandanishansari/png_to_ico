# Agent Instructions — PNG to ICO Converter

## Overview

Converts PNG images to multi-resolution ICO files (Windows icon format). The `core/` layer is directly runnable — no GUI needed. All scripts output JSON to stdout.

Run all commands from the **project root**.

## Prerequisites

- Python 3.x
- Dependencies installed: `pip install -r requirements.txt`

---

## Environment Variables

| Variable | Default | Description |
|---|---|---|
| `OUTPUT_FOLDER` | `output/` | Where the ICO file is written |

```powershell
# PowerShell
$env:OUTPUT_FOLDER = "./my_icons"
```
```bash
# bash
export OUTPUT_FOLDER="./my_icons"
```

---

## Scripts

### `core/converter.py` — Convert PNG to ICO

```bash
python core/converter.py logo.png icon.ico
```

```json
{"output_path": "output/icon.ico"}
```

**Input resolution:** bare filenames are looked up inside `input/`; full or relative paths are used as-is.

```bash
# These are equivalent if logo.png is in input/
python core/converter.py logo.png icon.ico
python core/converter.py input/logo.png icon.ico
```

**Output folder** respects `$OUTPUT_FOLDER` (default: `output/`). The folder is created automatically if it doesn't exist.

**Override sizes** with `--sizes` (comma-separated, square dimensions only):

```bash
python core/converter.py logo.png icon.ico --sizes 16,32,256
```

Default sizes: 16, 32, 48, 64, 128, 256.

```json
{"output_path": "output/icon.ico"}
```

---

## Workflow

```bash
# 1. Place PNG in input/
# 2. Run conversion
python core/converter.py logo.png icon.ico
# 3. ICO is at output/icon.ico (or $OUTPUT_FOLDER/icon.ico)
```

---

## Error Handling

All errors return `{"error": "<message>"}` and exit with code 1. Common causes:
- Input file not found in `input/` or at the given path
- Input file is not a PNG
- Invalid `--sizes` value
