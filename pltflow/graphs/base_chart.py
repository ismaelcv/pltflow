from __future__ import annotations  # To be able to do type annotations

from matplotlib import pyplot as plt

from pltflow.utils.styling import load_style


class chart:
    def __init__(self, style: str = "base") -> None:

        self.rcParams, self.styleParams, self.colors = load_style(style)
        plt.rcParams.update(plt.rcParamsDefault)
        self.set_figsize()

    def set_yticks(self, positions: list, **kwargs: dict) -> chart:
        self.styleParams["yticks"] = {**self.styleParams["yticks"], **{"ticks": positions}, **kwargs}
        return self

    def set_xticks(self, positions: list, **kwargs: dict) -> chart:
        self.styleParams["xticks"] = {**self.styleParams["xticks"], **{"ticks": positions}, **kwargs}
        return self

    def set_ylabel(self, label: str, **kwargs: dict) -> chart:
        self.styleParams["ylabel"] = {**self.styleParams["ylabel"], **{"ylabel": label}, **kwargs}
        return self

    def set_xlabel(self, label: str, **kwargs: dict) -> chart:
        self.styleParams["xlabel"] = {**self.styleParams["xlabel"], **{"xlabel": label}, **kwargs}
        return self

    def set_title(self, title: str, **kwargs: dict) -> chart:

        self.styleParams["title"] = {**self.styleParams["title"], **{"text": title}, **kwargs}

        return self

    def set_subtitle(self, subtitle: str) -> chart:
        self.styleParams["subtitle"]["text"] = subtitle

        return self

    def set_figsize(self, w: int = 9, h: int = 4) -> chart:
        if w > 0 and h > 0:
            self.rcParams["figure.figsize"] = (w, h)
        else:
            raise ValueError("w and h must be greater than 0")
        return self
