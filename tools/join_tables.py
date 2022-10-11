from astropy.table import Table, vstack
from pathlib import Path

TABLE_DIR = Path('data/output/')
ID_COL = "Cluster"

output_table = Table()

for table_path in TABLE_DIR.glob('*.csv'):
    
    name_id = table_path.stem
    table = Table.read(table_path, format="ascii")  # NOTICE pyUPMASK DEFAULT FORMAT IS ASCII
    table[ID_COL] = name_id
    
    output_table = vstack([output_table, table])

output_table.write(TABLE_DIR / "clusters.csv", format="csv", overwrite=True)
