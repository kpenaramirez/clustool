import inspect
import numpy as np
from enum import Enum

from dash import dcc, html

from . import ids
from .dropdown_helper import to_dropdown_options
from ..processing import PREPROCESSORS, CLUSTERERS

def generate_params_divs(function_names: list[str]) -> html.Div:
    
    components = []
    for fn_name in function_names:

        function_ = (PREPROCESSORS | CLUSTERERS)[fn_name]

        for p in inspect.signature(function_).parameters.values():
            pname = p.name
            ptype = p.annotation
            pdefaultvalue = None if (p.default is p.empty) else p.default

            if ptype is np.ndarray:
                continue

            if ptype is int:
                component = dcc.Input(
                    type="number",
                    placeholder=f"Integer",
                    value=pdefaultvalue,
                )
            elif ptype is float:
                component = dcc.Input(
                    type="number",
                    placeholder=f"Float",
                    value=pdefaultvalue,
                )
            elif issubclass(ptype, Enum):
                component = dcc.Dropdown(
                    options=to_dropdown_options(
                        [option.value for option in ptype.__members__.values()]
                    ),
                    value=pdefaultvalue.value,
                )

            components.append(html.Div([html.Label(pname), component]))
    
    return components