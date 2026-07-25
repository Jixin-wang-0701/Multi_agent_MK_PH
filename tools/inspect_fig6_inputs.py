from pathlib import Path
import sys

import pandas as pd


for input_name in sys.argv[1:]:
    path = Path(input_name)
    print(f"FILE {path.name}")
    workbook = pd.ExcelFile(path)
    print("SHEETS", ", ".join(workbook.sheet_names))
    for sheet_name in workbook.sheet_names:
        frame = pd.read_excel(path, sheet_name=sheet_name, header=None)
        print(f"SHEET {sheet_name}: {frame.shape}")
        print(frame.head(12).to_string(index=False, header=False))
