from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

from ..data.source import DataSource
from . import ids
from .dropdown_helper import to_dropdown_options_proc


def render(app: Dash, source: DataSource) -> html.Div:
    
    @app.callback(
        Output(ids.TEST_TEXT_BUTTON, "children"),
        Input(ids.RUN_BUTTON, "n_clicks"),
        State(ids.COLUMNS_SELECTION_DROPDOWN, "value"),
        State(ids.PREPROC_MULTI_DROPDOWN, "value"),
        State(ids.CLUSTERING_DROPDOWN, "value"),
        State(ids.CLUSTERING_PARAMS_DIV, "children"),
    )
    def press_button(
        n_clicks: int,
        columns:list[str],
        preproc_selection: list[str],
        clustering_selection: str,
        x,
    ) -> str:
        if n_clicks and columns and preproc_selection and clustering_selection:
            text = (
                f"Selected columns: {[c for c in columns]} "
                f"Selected preprocessing: {[p for p in preproc_selection]} "
                f"Selected clustering: {clustering_selection} "
                # f"x={x}"
            )
            
        else:
            text = "Please select all the options"
            
        return text

    return html.Div(
        children=[
            html.H5("Run clustering"),
            html.Button(
                "Run",
                id=ids.RUN_BUTTON,
                className="btn btn-primary"
            ),
            html.Div(
                id=ids.TEST_TEXT_BUTTON,
            )
        ]
    )