from dash import Dash, html
from src.components import (
    column_dropdown,
    preproc_selector,
    clustering_selector,
    run_button,
)

from ..data.source import DataSource


def create_layout(app: Dash, source: DataSource) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            column_dropdown.render(app, source),
            html.Hr(),
            preproc_selector.render(app, source),
            html.Hr(),
            clustering_selector.render(app, source),
            html.Hr(),
            run_button.render(app, source),
            html.Hr(),
            # html.Div(
            #     className="preproc-container",
            #     children=[
            #         preproc_selector.render(app, source),
            #     ],
            # ),
            # html.Div(
            #     className="cluster-container",
            #     children=[
            #         # Dropdown 
            #         # clustering options
            #     ],
            # ),
            # # Button start
            # html.Div(
            #     className="results-container",
            #     children=[
            #         # Scatter plot 1
            #         # Scatter plot 2
            #     ]
            # )            
        ],
    )
