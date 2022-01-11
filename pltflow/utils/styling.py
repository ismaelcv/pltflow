import importlib
from typing import Tuple


def load_style(style: str) -> Tuple[dict, dict, dict]:

    try:
        style_module = importlib.import_module(f"pltflow.styles.{style}").style  # type: ignore
    except ModuleNotFoundError as no_module_with_that_name:
        raise ModuleNotFoundError(f"Style {style} not found") from no_module_with_that_name

    return style_module["rcParams"], style_module["styleParams"], style_module["colors"]
