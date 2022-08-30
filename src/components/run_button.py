from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

from ..data.source import DataSource
from . import ids
from .dropdown_helper import to_dropdown_options_proc


def render(app: Dash, source: DataSource) -> html.Div:
    
    @app.callback(
        Output(ids.TEST_TEXT_BUTTON, "children"),
        Input(ids.RUN_BUTTON, "n_clicks"),
        State(ids.COLUMNS_SELECTION_DROPDOWN, "value")
    )
    def press_button(n_clicks: int, columns:list[str],) -> str:
        if n_clicks:
            return f"Selected columns: {[c for c in columns]}"

    return html.Div(
        children=[
            html.H6("Run clustering"),
            html.Button(
                "Run",
                id=ids.RUN_BUTTON,
            ),
            html.Div(
                id=ids.TEST_TEXT_BUTTON,
            )
        ]
    )