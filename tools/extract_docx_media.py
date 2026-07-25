from pathlib import Path
import sys
import zipfile


document_path = Path(sys.argv[1])
media_name = sys.argv[2]
output_path = Path(sys.argv[3])
with zipfile.ZipFile(document_path) as archive:
    with archive.open(f"word/media/{media_name}") as source, output_path.open("wb") as target:
        target.write(source.read())
