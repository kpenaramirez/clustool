import inspect
import numpy as np
from enum import Enum

from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from . import ids
from .autofun_helper import generate_params_divs
from .dropdown_helper import to_dropdown_options_proc
from ..data.source import DataSource
from ..processing import PREPROCESSORS


def render(app: Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(ids.PREPROC_PARAMS_DIV, "children"),
        Input(ids.PREPROC_MULTI_DROPDOWN, "value"),
    )
    def update_preprocessing_params(preproc_selection: list[str]) -> html.Div:
        """Update the corresponding list of parameters for each preprocessor function"""

        if preproc_selection is None:
            return html.Div()

        components = generate_params_divs(preproc_selection)

        return html.Div(components)

    return html.Div(
        children=[
            html.H6("Preprocessing algorithms"),
            dcc.Dropdown(
                id=ids.PREPROC_MULTI_DROPDOWN,
                options=to_dropdown_options_proc(PREPROCESSORS),
                multi=True,
                placeholder="None",
            ),
            html.Div(
                id=ids.PREPROC_PARAMS_DIV,
            ),
        ]
    )
