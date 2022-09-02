from .preprocesors import standar_scaler

from .clusterers import (
    kmeans_,
    dbscan_,
    optics_,
    hdbscan_,
    gmm_,
)

PREPROCESSORS = {
    "Standar Scaler": standar_scaler,
}

CLUSTERERS = {
    "KMeans": kmeans_,
    "DBSCAN": dbscan_,
    # "OPTICS": optics_,  # it takes too long
    "HDBSCAN": hdbscan_,
    "GMM": gmm_,
}
