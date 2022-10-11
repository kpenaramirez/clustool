from __future__ import annotations

from dataclasses import dataclass, field
from functools import partial, reduce
from datetime import datetime
from typing import Callable

import pandas as pd
import numpy as np


Processor = Callable[[np.ndarray], np.ndarray]
DEFAULT_GROUP: int = -2


def compose(*functions: Processor) -> Processor:
    return reduce(lambda f, g: lambda x: g(f(x)), functions)


@dataclass
class DataSource:
    _data: pd.DataFrame
    _cols: list[str] = field(init=False)

    def __post_init__(self):
        self._cols = list(self._data.columns)
        self._data["result"] = DEFAULT_GROUP

    def _filter_dataframe(self, columns: list[str], cluster: str) -> pd.DataFrame:
        """Filter the dataframe including selected columns and remove rows that contain NaN"""

        df = self._data.copy()
        df = df.query("Cluster == @cluster")  # Select only rows with the selected cluster
        df = df[columns].dropna()  # Remove nan rows

        return df

    def process(self, columns: list[str], cluster: str, *functions: Processor) -> None:
        """Process the data using the functions in the same order as provided"""

        print(f"{datetime.now()} Processing data {cluster}")
        self._data["result"] = DEFAULT_GROUP  # reset results
        preproc_df = self._filter_dataframe(columns, cluster)
        processor = compose(*functions)
        result = processor(preproc_df.to_numpy())
        self._data.loc[preproc_df.index.values, "result"] = result

    @property
    def all_columns(self) -> list[str]:

        list_of_columns = self._cols.copy()
        for element in ["Cluster", "probs_final"]:
            if element in list_of_columns:
                list_of_columns.remove(element)
        
        return list_of_columns

    @property
    def get_data(self) -> pd.DataFrame:
        return self._data.copy()
    
    @property
    def all_cluster_names(self) -> list[str]:
        return self._data["Cluster"].unique().tolist()
