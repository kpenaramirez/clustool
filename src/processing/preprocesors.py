import numpy as np
from sklearn.preprocessing import StandardScaler

"""
Preprocessing functions. No parameters allowed! 
"""

class NanValueEncounterError(Exception):
    pass


def standar_scaler(data: np.ndarray) -> np.ndarray:
    """Apply standar scaling to the data."""

    scaler = StandardScaler().fit(data)
    scaled_data = scaler.transform(data)

    if np.any(np.isnan(scaled_data)):
        raise NanValueEncounterError(
            "Standar scaler produced NaN values. Check your data"
        )

    return scaled_data
