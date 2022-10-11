from dash import Dash, dcc, html

from ..data.source import DataSource
from . import ids
from .dropdown_helper import to_dropdown_options


def render(app: Dash, source: DataSource) -> html.Div:

    return html.Div(
        children=[
            html.H5("Cluster Selection"),
            dcc.Dropdown(
                id=ids.CLUSTER_SELECTION_DROPDOWN,
                options=to_dropdown_options(source.all_cluster_names),
                value=source.all_cluster_names[0],
                multi=False,
                placeholder="Select Cluster",
            ),
        ]
    )
