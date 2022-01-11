from __future__ import annotations

from typing import Optional, Union

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from pltflow.utils.styling import load_style


class chart:
    def __init__(
        self,
        data: Union[pd.DataFrame, list, np.ndarray, pd.Series],
        x: Optional[str] = "",
        y: Optional[str] = "",
        style: str = "base",
    ) -> None:

        self.rcParams, self.styleParams, self.colors = load_style(style)
        plt.rcParams.update(plt.rcParamsDefault)
        self.set_figsize()

        self.set_parameters(data, x, y)
        self.z = ""  # type: str
        self.main_categories = []  # type: list
        self.mode = "default"  # type: str

    def set_parameters(
        self,
        data: Union[pd.DataFrame, list, np.ndarray, pd.Series],
        x: Optional[str],
        y: Optional[str],
    ) -> None:
        """
        This parameters are set for the case of scatterplots.
        In this mode the only valid input is a dataframe
        """

        if isinstance(data, pd.DataFrame):
            self.df = data
        else:
            raise ValueError("color_by() can only be used with a dataframe as data source")

        if x in self.df.columns:
            self.x = x
        else:
            raise ValueError("X and Y should be a valid column name")

        if y in self.df.columns:
            self.y = y
        else:
            raise ValueError("X and Y should be a valid column name")

        self.set_xlabel(x)
        self.set_ylabel(y)

    def set_mode(self, mode: str) -> None:

        if mode in ["default", "scatter", "line"]:
            self.mode = mode
        else:
            raise ValueError("mode must be either 'default', 'scatter' or 'line'")

    def set_yticks(self, positions: list, **kwargs: dict) -> chart:
        self.styleParams["yticks"] = {**self.styleParams["yticks"], **{"ticks": positions}, **kwargs}
        return self

    def set_xticks(self, positions: list, **kwargs: dict) -> chart:
        self.styleParams["xticks"] = {**self.styleParams["xticks"], **{"ticks": positions}, **kwargs}
        return self

    def set_ylabel(self, label: Optional[str], **kwargs: dict) -> chart:

        if label not in ("", None):
            self.styleParams["ylabel"] = {**self.styleParams["ylabel"], **{"ylabel": label}, **kwargs}
        return self

    def set_xlabel(self, label: Optional[str], **kwargs: dict) -> chart:

        if label not in ("", None):
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

    def color_by(self, column_name: str) -> chart:
        """
        Set the color for the plot.
        """

        if not isinstance(self.df, pd.DataFrame):
            raise ValueError("color_by() can only be used with a dataframe as data source")

        if column_name not in self.df.columns:
            raise ValueError(f"{column_name} not in dataframe")

        self.z = column_name

        self.styleParams["color_by"] = column_name

        if self.main_categories == []:
            self.main_categories = list(self.df[column_name].unique())

        available_values = list(
            self.df.loc[self.df[self.z].isin(self.main_categories), self.z].value_counts().index
        )

        if len(self.main_categories) > 20:
            print(
                f"Posible categories to .focus_on()  {available_values[:20]} and {len(self.main_categories) - 20} more"
            )
        else:
            print(f"Possible categories to .focus_on() {available_values}")

        return self

    def focus_on(self, category: Union[str, list]) -> chart:
        """
        Set the main category for the plot.

        """
        if not isinstance(self.df, pd.DataFrame):
            raise ValueError("color_by() can only be used with a dataframe as data source")

        all_cats_available = list(self.df[self.z].unique())

        if self.main_categories == all_cats_available:
            self.main_categories = []

        if isinstance(category, str):

            if category not in all_cats_available:
                raise ValueError(
                    f"{category} is not included on the main categories avalable in the {self.z} column"
                )
            self.main_categories.append(category)

        elif isinstance(category, list):

            invalid_categories = []
            for requested_cat in category:
                if requested_cat not in all_cats_available:
                    invalid_categories.append(requested_cat)

            if len(invalid_categories) > 0:
                raise ValueError(
                    f"{invalid_categories} does not form part of the available categories of  the column {self.x}"
                )

            self.main_categories.append(category)

        self.main_categories = list(pd.Series(self.main_categories).unique())

        return self
