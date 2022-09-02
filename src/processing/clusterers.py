from enum import Enum

import hdbscan
import numpy as np
from sklearn import cluster, mixture


def kmeans_(data: np.ndarray, n_clusters: int = 3) -> np.ndarray:
    """Apply KMeans to the data."""

    kmeans = cluster.KMeans(n_clusters=n_clusters).fit(data)
    labels = kmeans.labels_

    return labels


def dbscan_(data: np.ndarray, eps: float = 0.5, min_samples: int = 5) -> np.ndarray:
    """Apply DBSCAN to the data."""

    clusterer = cluster.DBSCAN(eps=eps, min_samples=min_samples).fit(data)
    labels = clusterer.labels_

    return labels


def optics_(
    data: np.ndarray,
    min_samples: int = 5,
    xi: float = 0.05,  # float between 0 and 1
    min_cluster_size: float = 0.05, 
) -> np.ndarray:
    """Apply OPTICS to the data."""

    clusterer = cluster.OPTICS(min_samples=min_samples, xi=xi, min_cluster_size=min_cluster_size).fit(data)
    labels = clusterer.labels_

    return labels


class CSMParams(Enum):
    EOM = "eom"
    LEAF = "leaf"


def hdbscan_(
    data: np.ndarray,
    min_cluster_size: int = 3,
    min_samples: int = 0,
    cluster_selection_method: CSMParams = CSMParams.EOM,  # "eom" or "leaf"
) -> np.ndarray:
    """Apply HDBSCAN to the data."""

    clusterer = hdbscan.HDBSCAN(
        min_cluster_size=min_cluster_size,
        min_samples=min_samples,
        cluster_selection_method=cluster_selection_method,
    ).fit(data)
    labels = clusterer.labels_

    return labels


class CovarianceType(Enum):
    FULL = "full"
    TIED = "tied"
    DIAG = "diag"
    SPHERICAL = "spherical"


def gmm_(
    data: np.ndarray,
    n_components: int = 1,
    covariance_type: CovarianceType = CovarianceType.FULL,
) -> np.ndarray:
    """Apply Gaussian mixture model to the data."""

    clusterer = mixture.GaussianMixture(
        n_components=n_components,
        covariance_type=covariance_type,
        tol=1e-3,
        reg_covar=1e-6,
        max_iter=100,
        n_init=1,
        init_params="kmeans",
    ).fit(data)
    labels = clusterer.predict(data)

    return labels
