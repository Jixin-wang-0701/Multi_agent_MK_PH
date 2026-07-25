from pathlib import Path
import sys

import pypdfium2 as pdfium


source = Path(sys.argv[1])
target = Path(sys.argv[2])
page_number = int(sys.argv[3]) if len(sys.argv) > 3 else 0
document = pdfium.PdfDocument(source)
page = document[page_number]
bitmap = page.render(scale=2.0, rotation=0)
bitmap.to_pil().convert("RGB").save(target, "PNG")
