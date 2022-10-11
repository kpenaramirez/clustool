This directory contains tools for preprocesing the data and construct the input catalog for the dashboard.

- `create_input_data.py`: Script to convert the raw catalogs (combis) into a smaller sample centered around the central coordinates of each cluster. Rows with nan values are removed. 
- `cluster_selection.yaml`: Configuration file for the cluster selection. Parameters: name, ra, dec and r50.
- `params_pyUPMASK.ini`: Configuration file for pyUPMASK external software. Run pyUPMASK for selected clusters in order to precompute the probabilities with vanilla hyperparameters.
- `join_tables.py`: Script to join tables into a single catalog. Resulting catalog is used as input for the dashboard.