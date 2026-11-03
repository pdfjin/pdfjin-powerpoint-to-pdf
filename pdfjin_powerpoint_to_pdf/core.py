import subprocess
from pathlib import Path
from typing import Union


def convert_pptx_to_pdf(input_pptx: Union[str, Path], output_pdf: Union[str, Path]) -> Path:
    in_p = Path(input_pptx).resolve()
    out_p = Path(output_pdf).resolve()
    out_p.parent.mkdir(parents=True, exist_ok=True)

    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(out_p.parent), str(in_p)], check=True)
    return out_p
