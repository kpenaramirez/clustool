from .preprocesors import standar_scaler

from .clusterers import (
    kmeans_,
    dbscan_,
    optics_,
    hdbscan_,
    gmm_,
    minibatch_kmeans_,
    bayesian_gaussian_mixture_,
    birch_,
)

PREPROCESSORS = {
    "Standar Scaler": standar_scaler,
}

CLUSTERERS = {
    "KMeans": kmeans_,
    "DBSCAN": dbscan_,
    "OPTICS": optics_,  # it takes too long
    "HDBSCAN": hdbscan_,
    "GaussianMixture": gmm_,
    "MiniBatchKMeans": minibatch_kmeans_,
    "BayesianGaussianMixture": bayesian_gaussian_mixture_,
    "Birch": birch_,
}
