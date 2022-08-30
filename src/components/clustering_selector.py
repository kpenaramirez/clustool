from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data.source import DataSource
from . import ids
from .dropdown_helper import to_dropdown_options_proc

from ..processing import CLUSTERERS

def render(app: Dash, source: DataSource) -> html.Div:

    return html.Div(
        children=[
            html.H6("Preprocessing algorithms"),
            dcc.Dropdown(
                id=ids.CLUSTERING_DROPDOWN,
                options=to_dropdown_options_proc(CLUSTERERS),
                # value=None,
                multi=False,
                placeholder="Select a clustering algorithm",
            ),
        ]
    )