from pathlib import Path

from PIL import Image

DEFAULT_SIZES = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]


def convert(input_path: str, output_path: str, sizes: list[tuple[int, int]] = None) -> str:
    """
    Convert a PNG to a multi-resolution ICO file.

    Transparency is preserved. Returns the output path.
    """
    if sizes is None:
        sizes = DEFAULT_SIZES

    path = Path(input_path)
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    if path.suffix.lower() != ".png":
        raise ValueError(f"Unsupported format: {path.suffix!r}. Only PNG is supported.")

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    img = Image.open(input_path).convert("RGBA")
    img.save(output_path, format="ICO", sizes=sizes)
    return output_path


if __name__ == "__main__":
    import argparse
    import json
    import os
    import sys

    parser = argparse.ArgumentParser(description="Convert a PNG file to ICO format")
    parser.add_argument("input_file", help="Input PNG file (filename inside input/ or a full path)")
    parser.add_argument("output_file", help="Output ICO filename")
    parser.add_argument(
        "--sizes",
        type=str,
        default=None,
        help="Comma-separated icon sizes to include, e.g. 16,32,48,256 (default: 16,32,48,64,128,256)",
    )
    args = parser.parse_args()

    # Resolve input — bare filename looks in input/, full/relative paths used as-is
    input_path = Path(args.input_file)
    if not input_path.exists():
        input_path = Path("input") / args.input_file

    # Resolve output folder from env, fallback to output/
    output_folder = Path(os.environ.get("OUTPUT_FOLDER", "output"))
    output_path = output_folder / Path(args.output_file).name

    # Parse optional sizes override
    sizes = DEFAULT_SIZES
    if args.sizes:
        try:
            sizes = [(int(x.strip()), int(x.strip())) for x in args.sizes.split(",")]
        except ValueError:
            print(json.dumps({"error": f"Invalid --sizes value: {args.sizes!r}"}))
            sys.exit(1)

    try:
        result = convert(str(input_path), str(output_path), sizes)
        print(json.dumps({"output_path": result}))
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)
