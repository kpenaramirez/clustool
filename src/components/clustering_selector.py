from dash import Dash, dcc, html
from dash.dependencies import Input, Output


from . import ids
from .autofun_helper import generate_params_divs
from .dropdown_helper import to_dropdown_options_proc
from ..data.source import DataSource
from ..processing import CLUSTERERS

def render(app: Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(ids.CLUSTERING_PARAMS_DIV, "children"),
        Input(ids.CLUSTERING_DROPDOWN, "value"),
    )
    def update_clustering_params(clustering_selection: str) -> html.Div:
        """Update the corresponding list of parameters for each clustering function"""

        if clustering_selection is None:
            return html.Div()

        print(clustering_selection)
        components = generate_params_divs([clustering_selection])

        return html.Div(components)
    
    return html.Div(
        children=[
            html.H5("Preprocessing algorithms"),
            dcc.Dropdown(
                id=ids.CLUSTERING_DROPDOWN,
                options=to_dropdown_options_proc(CLUSTERERS),
                # value=None,
                multi=False,
                placeholder="Select a clustering algorithm",
            ),
            html.Div(
                id=ids.CLUSTERING_PARAMS_DIV,
            ),
        ]
    )