from enum import Enum

import hdbscan
import numpy as np
from sklearn.cluster import KMeans


def kmeans_(data: np.ndarray, n_clusters: int = 3) -> np.ndarray:
    """Apply KMeans to the data."""

    kmeans = KMeans(n_clusters=n_clusters).fit(data)
    labels = kmeans.labels_

    return labels


class SelectionMethod(Enum):
    EOM = "eom"
    LEAF = "leaf"


def hdbscan_(
    data: np.ndarray,
    min_cluster_size: int = 3,
    min_samples: int | None = None,
    cluster_selection_method: SelectionMethod = SelectionMethod.EOM,
) -> np.ndarray:
    """Apply HDBSCAN to the data."""

    clusterer = hdbscan.HDBSCAN(
        min_cluster_size=min_cluster_size,
        min_samples=min_samples,
        cluster_selection_method=cluster_selection_method.value,
    ).fit(data)
    labels = clusterer.labels_

    return labels
