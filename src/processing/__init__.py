from .preprocesors import standar_scaler

from .clusterers import (
    kmeans_,
    dbscan_,
    optics_,
    hdbscan_,
)

PREPROCESSORS = {
    "Standar Scaler": standar_scaler,
}

CLUSTERERS = {
    "KMeans": kmeans_,
    "DBSCAN": dbscan_,
    "OPTICS": optics_,
    "HDBSCAN": hdbscan_,
}