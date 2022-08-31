from html.entities import html5
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data.source import DataSource
from . import ids


def render(app: Dash, source: DataSource) -> html.Div:

    @app.callback(
        Output(ids.SCATTER_GRAPH, "figure"),
        Input(ids.PLOT_BUTTON, "n_clicks"),
    )
    def update_graph(n_clicks: int) -> px.scatter:
        """Update the scatter graph with the new data"""
        df = source.get_data
        df["result"] = df["result"].astype(str)
        return px.scatter(
            df,
            x="ra",
            y="dec",
            color="result",
            opacity=0.05,
        )

    return html.Div(
        children=[
            html.H5("Plot"),
            html.Button("Plot", id=ids.PLOT_BUTTON, className="btn btn-secondary"),
            dcc.Graph(
                id=ids.SCATTER_GRAPH,
            )
        ]
    )

