from __future__ import annotations

from dataclasses import dataclass, field
from functools import partial, reduce
from typing import Callable

import pandas as pd
import numpy as np


Processor = Callable[[np.ndarray], np.ndarray]

def compose(*functions: Processor) -> Processor:
    return reduce(lambda f, g: lambda x: g(f(x)), functions)


@dataclass
class DataSource:
    _data: pd.DataFrame
    _cols: list[str] = field(init=False)

    def __post_init__(self):
        self._cols = list(self._data.columns)
        self._data["result"] = -1

    def _filter_dataframe(self, columns: list[str]) -> pd.DataFrame:
        """Filter the dataframe including selected columns and remove rows that contain NaN"""
       
        df = self._data.copy()
        df = df[columns].dropna()  # Remove nan rows

        return df
    
    def process(self, columns: list[str], *functions: Processor)-> None:
        """Process the data using the functions in the same order as provided"""

        preproc_df = self._filter_dataframe(columns)
        processor = compose(*functions)
        result = processor(preproc_df.to_numpy())
        self._data.loc[preproc_df.index.values, "result"] = result


    @property
    def all_columns(self) -> list[str]:
        return self._cols

    @property
    def get_data(self) -> pd.DataFrame:
        return self._data.copy()

