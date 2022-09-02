from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

from functools import partial


from . import ids
from ..data.source import DataSource
from ..processing import PREPROCESSORS, CLUSTERERS


def render(app: Dash, source: DataSource) -> html.Div:

    @app.callback(
        Output(ids.RUN_BUTTON, 'disabled'),
        Output(ids.RUN_BUTTON, 'children'),
        Output(ids.RUN_BUTTON, 'className'),
        Input(ids.RUN_BUTTON, "n_clicks"),
    )
    def hide_newbutton(n_clicks: int) -> bool:
        if n_clicks is None:
            return False, "RUN", "btn btn-primary"
        else:
            return True, "Running", "btn btn-light"

    @app.callback(
        Output(ids.RESPONSE_TEXT_BUTTON, "children"),
        Output(ids.RESPONSE_TEXT_BUTTON, "className"),
        Output('dynamic-button-container', 'children'),
        Input(ids.RUN_BUTTON, "n_clicks"),
        State(ids.COLUMNS_SELECTION_DROPDOWN, "value"),
        State(ids.PREPROC_DROPDOWN, "value"),
        State(ids.PREPROC_PARAMS_DIV, "children"),
        State(ids.CLUSTERING_DROPDOWN, "value"),
        State(ids.CLUSTERING_PARAMS_DIV, "children"),
        State('dynamic-button-container', 'children'),
    )
    def press_button(
        n_clicks: int,
        columns: list[str],
        preproc_selection: str,
        preproc_div: dict,
        clustering_selection: str,
        clustering_div: dict,
        children: html.Div,
    ) -> tuple[str, str, html.Div]:
        """Run the preprocessing and clustering using the definded functions and respective parameters"""

        
        pipeline = []

        # Trick to disable the button
        new_button = html.Button(
            "Run",
            id = ids.RUN_BUTTON, 
            className="btn btn-primary",
            style={"margin-right": "10px", "width": "100px"},
		)

        children.pop()
        children.append(new_button)

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
                    clustering_div["props"]["children"][i]["props"]["children"][1][
                        "props"
                    ][
                        "value"
                    ]  # FIXME: this is ugly
                    for i in range(n_cluster_params)
                ]
                clustering_params_names = [
                    clustering_div["props"]["children"][i]["props"]["children"][0][
                        "props"
                    ]["children"]
                    for i in range(n_cluster_params)
                ]
                clustering_params = dict(
                    zip(clustering_params_names, clustering_params_values)
                )

                if any(p is None for p in clustering_params_values):
                    return "Please fill all the parameters", "alert alert-warning", children

                pipeline.append(partial(clustering_function, **clustering_params))

                # Run the pipeline
                try:
                    source.process(columns, *pipeline)
                    return f"Success!", "alert alert-success", children
                except Exception as e:
                    return f"Error: {e}", "alert alert-danger", children

            else:
                return (
                    "Please select columns and a clustering algorithm",
                    "alert alert-warning",
                    children,
                )

        else:
            return "", "", children

    return html.Div(
        children=[
            html.H5("Excecute"),
            html.Div(
                id='dynamic-button-container',
                children=[
                    html.Button(
                        "Run",
                        id=ids.RUN_BUTTON,
                        className="btn btn-primary",
                        style={"margin-right": "10px", "width": "100px"},
                    ),
                ]
            ),
            html.H5(""),
            html.Div(id=ids.RESPONSE_TEXT_BUTTON, style={"margin-top": "5px"}),
        ]
    )
