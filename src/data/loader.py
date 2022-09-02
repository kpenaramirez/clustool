import pandas as pd


def load_input_data(path: str) -> pd.DataFrame:
    """Load data from the CSV file"""

    data = pd.read_csv(
        path,
    )

    return data
