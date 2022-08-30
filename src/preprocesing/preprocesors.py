import numpy as np

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


class NanValueEncounterError(Exception):
    pass


def standar_scaler(data: np.ndarray) -> np.ndarray:
    """Apply standar scaling to the data."""
    
    scaler = StandardScaler().fit(data)
    scaled_data = scaler.transform(data)
    
    if np.any(np.isnan(scaled_data)):
        raise NanValueEncounterError("Standar scaler produced NaN values. Check your data")

    return scaled_data


def dim_reduction_pca(data: np.ndarray, n_components: int = 3) -> np.ndarray:
    """Apply PCA to the data."""
    
    pca = PCA(n_components=n_components).fit(data)
    reduced_data = pca.transform(data)
    
    if np.any(np.isnan(reduced_data)):
        raise NanValueEncounterError("PCA produced NaN values. Check your data")

    return reduced_data