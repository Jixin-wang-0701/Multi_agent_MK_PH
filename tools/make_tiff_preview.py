from pathlib import Path
import sys

from PIL import Image


source = Path(sys.argv[1])
target = Path(sys.argv[2])
image = Image.open(source).convert("RGB")
image.thumbnail((1800, 1800))
image.save(target, "PNG", optimize=True)
