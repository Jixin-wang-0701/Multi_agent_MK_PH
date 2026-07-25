from pathlib import Path
import sys
import zipfile

from lxml import etree


NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}

with zipfile.ZipFile(Path(sys.argv[1])) as archive:
    doc = etree.fromstring(archive.read("word/document.xml"))
    rels = etree.fromstring(archive.read("word/_rels/document.xml.rels"))
    lookup = {
        item.get("Id"): item.get("Target")
        for item in rels
        if item.get("Type", "").endswith("/image")
    }
    for index, paragraph in enumerate(doc.xpath(".//w:p", namespaces=NS)):
        text = "".join(paragraph.xpath(".//w:t/text()", namespaces=NS)).strip()
        embeds = paragraph.xpath(".//a:blip/@r:embed", namespaces=NS)
        if embeds:
            print(index, text[:150], [lookup.get(key) for key in embeds])
