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
    _selected_cols: list[str] = field(init=False)

    def __post_init__(self):
        self._selected_cols = list(self._data.columns)

    def _filter_dataframe(self, columns: list[str]) -> pd.DataFrame:
        """Filter the dataframe including selected columns and remove rows that contain NaN"""
       
        df = self._data.copy()
        df = df[columns].dropna()  # Remove nan rows

        return df
    
    def process(self, *functions: Processor)-> DataSource:
        """Process the data using the functions in the same order as provided"""

        preproc_df = self._filter_dataframe(self._selected_cols)
        processor = compose(*functions)
        result = processor(preproc_df.values)
        preproc_df["result"] = result
        return DataSource(preproc_df)


    @property
    def all_columns(self) -> list[str]:
        return list(self._data.columns)

