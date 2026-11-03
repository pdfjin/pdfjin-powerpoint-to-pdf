import sys, argparse
try:
    from .core import convert_pptx_to_pdf
    from . import __version__
except (ImportError, ValueError):
    from pdfjin_powerpoint_to_pdf.core import convert_pptx_to_pdf
    from pdfjin_powerpoint_to_pdf import __version__


def main():
    p = argparse.ArgumentParser(prog="pdfjin-powerpoint-to-pdf", description="Convert PPTX to PDF.")
    p.add_argument("input", help="Input PPTX file")
    p.add_argument("-o", "--output", required=True, help="Output PDF file")
    p.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    args = p.parse_args()
    try:
        convert_pptx_to_pdf(args.input, args.output)
        print(f"PDF saved -> {args.output}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr); sys.exit(1)


if __name__ == "__main__":
    main()
