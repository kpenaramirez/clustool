from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

from functools import partial


from . import ids
from ..data.source import DataSource
from ..processing import PREPROCESSORS, CLUSTERERS


def render(app: Dash, source: DataSource) -> html.Div:

    @app.callback(
        Output(ids.RESPONSE_TEXT_BUTTON, "children"),
        Output(ids.RESPONSE_TEXT_BUTTON, "className"),
        Input(ids.RUN_BUTTON, "n_clicks"),
        State(ids.COLUMNS_SELECTION_DROPDOWN, "value"),
        State(ids.PREPROC_DROPDOWN, "value"),
        State(ids.PREPROC_PARAMS_DIV, "children"),
        State(ids.CLUSTERING_DROPDOWN, "value"),
        State(ids.CLUSTERING_PARAMS_DIV, "children"),
    )
    def press_button(
        n_clicks: int,
        columns: list[str],
        preproc_selection: str,
        preproc_div: dict,
        clustering_selection: str,
        clustering_div: dict,
    ) -> tuple[str, str]:
        """Run the preprocessing and clustering using the definded functions and respective parameters"""

        pipeline = []

        if n_clicks:
            if columns and clustering_selection:

                # Preprocessing
                if preproc_selection:
                    preproc_func = PREPROCESSORS[preproc_selection]
                    pipeline.append(preproc_func)

                # Clustering
                n_cluster_params = len(clustering_div["props"]["children"])
                clustering_function = CLUSTERERS[clustering_selection]
                clustering_params_values = [
                    clustering_div["props"]["children"][i]["props"]["children"][1]["props"]["value"]  # FIXME: this is ugly
                    for i in range(n_cluster_params)
                ]
                clustering_params_names = [
                    clustering_div["props"]["children"][i]["props"]["children"][0]["props"]["children"]
                    for i in range(n_cluster_params)
                ]
                clustering_params = dict(zip(clustering_params_names, clustering_params_values))

                if any(p is None for p in clustering_params_values):
                    return "Please fill all the parameters", "alert alert-warning"

                pipeline.append(partial(clustering_function, **clustering_params))

                text = (
                    # f"Selected columns: {[c for c in columns]} "
                    # f"Selected preprocessing: {[p for p in preproc_selection]} "
                    # f"Selected clustering: {clustering_selection} "
                    # =f"x={clustering_div}"
                    # f"{clustering_function}{clustering_params_values}"
                    f"{pipeline}"
                )

                # Run the pipeline
                try:
                    source.process(columns, *pipeline)
                    return "Success", "alert alert-success"
                except Exception as e:
                    return f"Error: {e}", "alert alert-danger"

            else:
                return "Please select columns and a clustering", "alert alert-warning"
        
        else:
            return "", ""


    return html.Div(
        children=[
            html.H5("Run clustering"),
            html.Button("Run", id=ids.RUN_BUTTON, className="btn btn-primary"),
            html.Div(
                id=ids.RESPONSE_TEXT_BUTTON,
            ),
        ]
    )
