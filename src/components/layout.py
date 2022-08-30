from dash import Dash, html
from src.components import (
    column_dropdown,
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
                    
                ],
            ),
        ],
    )
