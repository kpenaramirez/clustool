from dash import Dash, html, dcc
from src.components import (
    cluster_selection_dropdown,
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
            dcc.Markdown(f"# {app.title}", mathjax=True),
            dcc.Markdown(f"Peña Ramírez et al. (2020 and 2021)"),
            html.Div(
                [cluster_selection_dropdown.render(app, source)],
            ),
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
