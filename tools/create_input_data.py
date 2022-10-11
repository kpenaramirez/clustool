from pathlib import Path
import pandas as pd
import yaml


from dataclasses import dataclass, field

from astropy.coordinates import SkyCoord
from astropy.table import Table
from astropy import units as u


DATA_DIR = Path("/home/jorge/Documents/data/combi/")
OUTPUT_DIR = Path("data/input/")
TIMES_R50 = 2.0

@dataclass
class StarCluster:
    """Star cluster representation"""
    name: str
    ra: float
    dec: float
    r50: float
    table: Table = field(init=False)
    coord: SkyCoord = field(init=False)

    def __post_init__(self):
        """Load the data from the file and compute coordinates"""

        table_path_gen = DATA_DIR.glob(f"{self.name}*combi.csv.gz")
        self.table = Table.read(next(table_path_gen), format="csv")

        self.coord = SkyCoord(self.ra, self.dec, unit="deg")


def get_coordinates(table: Table) -> SkyCoord:
    """Get coordinates from ra and dec"""
    return SkyCoord(
        table["ra"],
        table["dec"],
        unit="deg",
        frame="icrs",
    )

def cone_search(table: Table, coordinates: SkyCoord, radius: float) -> Table:
    """Perform a cone search and return a new table with the results."""
    return table[coordinates.separation(get_coordinates(table)) < radius * u.deg]

def dropna(table: Table) -> Table:
    """Remove rows with NaN values"""
    df = table.to_pandas()
    df.dropna(inplace=True)
    return Table.from_pandas(df)

def add_galactic_coordinates(table: Table) -> Table:
    """Get galactic coordinates from ra and dec"""
    coords = get_coordinates(table)
    table["l"] = coords.galactic.l.deg
    table["b"] = coords.galactic.b.deg
    return table

def process(cluster: StarCluster, output_dir: Path = OUTPUT_DIR) -> None:
    """Process a single cluster"""
    table = cone_search(cluster.table, cluster.coord, cluster.r50 * TIMES_R50)
    table = dropna(table)
    table = add_galactic_coordinates(table)
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    table.write(output_dir / f"{cluster.name}.csv", format="csv")


def main() -> None:

    # Load cluster selection file
    with open(Path("tools/cluster_selection.yaml")) as file:
        file_content = yaml.load(file, Loader=yaml.FullLoader)
        clusters = [StarCluster(**c) for c in file_content]
    
    for cluster in clusters:
        process(cluster)


if __name__ == "__main__":
    main()