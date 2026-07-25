from pathlib import Path
import sys

import pandas as pd


input_path = Path(sys.argv[1])
output_path = Path(sys.argv[2])
data = pd.read_excel(input_path)
row = data.loc[data["compound"].astype(str).str.casefold().eq("methionine")]
if row.shape[0] != 1:
    raise ValueError("Expected exactly one methionine row in the metabolomics workbook.")

row = row.iloc[0]
records = []
for group, columns in {
    "Control MK": ["Control-mk-1", "Control-mk-2", "Control-mk-3"],
    "PH MK": ["PH-mk-1", "PH-mk-2", "PH-mk-3"],
}.items():
    for column in columns:
        records.append({"group": group, "sample": column, "intensity": float(row[column])})

output_path.parent.mkdir(parents=True, exist_ok=True)
pd.DataFrame(records).to_csv(output_path, index=False)
