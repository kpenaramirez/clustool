from dash import Dash, html
from src.components import (
    column_dropdown,
    ids,
    preproc_selector,
    clustering_selector,
    run_button,
    scatter_graph_l,
    scatter_graph_r,
)


from ..data.source import DataSource


def create_layout(app: Dash, source: DataSource) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    column_dropdown.render(app, source),
                    preproc_selector.render(app, source),
                    clustering_selector.render(app, source),
                    run_button.render(app, source),
                ],
            ),
            html.Hr(),
            html.Button(
                "Plot",
                id=ids.PLOT_BUTTON,
                className="btn btn-primary",
                style={"width": "120px"},
            ),
            html.Div(
                className="graph-container",
                children=[
                    scatter_graph_l.render(app, source),
                    scatter_graph_r.render(app, source),
                ],
            ),
        ],
    )
