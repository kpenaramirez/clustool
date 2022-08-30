from .preprocesors import standar_scaler, dim_reduction_pca

from .clusterers import (
    kmeans_,
    dbscan_,
    optics_,
    hdbscan_,
)

PREPROCESSORS = {
    "Standar Scaler": standar_scaler,
    "DimRed PCA": dim_reduction_pca,
}

CLUSTERERS = {
    "KMeans": kmeans_,
    "DBSCAN": dbscan_,
    "OPTICS": optics_,
    "HDBSCAN": hdbscan_,
}