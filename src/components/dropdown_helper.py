from typing import Callable

def to_dropdown_options(values: list[str]) -> list[dict[str, str]]:
    return [{"label": value.replace("_", " "), "value": value} for value in values]

def to_dropdown_options_proc(procs: dict[str, Callable]) -> list[dict[str, str]]:
    return [{"label": k.replace("_", " "), "value": k} for k in procs.keys()]

