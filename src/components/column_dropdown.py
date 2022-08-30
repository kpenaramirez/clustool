from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data.source import DataSource
from . import ids
from .dropdown_helper import to_dropdown_options

def render(app: Dash, source: DataSource) -> html.Div:

    return html.Div(
        children=[
            html.H6("Columns Selection"),
            dcc.Dropdown(
                id=ids.COLUMNS_SELECTION_DROPDOWN,
                options=to_dropdown_options(source.all_columns),
                value=source.all_columns,
                multi=True,
                placeholder="Select parameters to cluster",
            ),
        ]
    )
