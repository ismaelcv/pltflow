from __future__ import annotations  # To be able to do type annotations

from typing import Optional, Union

import numpy as np
import pandas as pd
from base_chart import chart
from matplotlib import pyplot as plt
from utils.data_checks import check_array_is_numeric

from pltflow.utils.preprocess import set_main_categories
from pltflow.utils.styling import load_style


class hist(chart):

    """
    Generic class to genererate an histogram in style
    """

    def __init__(
        self,
        data: Union[pd.DataFrame, list, np.ndarray, pd.Series],
        x: Optional[str] = "",
        style: str = "base",
        mode: str = "line",
    ) -> None:

        self.rcParams, self.styleParams, self.colors = load_style(style)

        plt.rcParams.update(plt.rcParamsDefault)

        if isinstance(data, pd.DataFrame):
            self.df = data
            self.x = x

            if self.x == "":
                raise ValueError("x must be a name of a column in the dataframe")

            self.set_xlabel(self.x)  # type: ignore

        else:
            check_array_is_numeric(data)
            self.df = data
            self.x = "x"
            self.set_xlabel("")

        self._set_mode(mode)
        self.set_ylabel("frecuency")
        self.set_figsize()
        self.z = ""  # type: str
        self.main_categories = []  # type: list

    def _set_mode(self, mode: str) -> hist:

        if mode in ["both", "bars", "line"]:
            self.mode = mode
        else:
            raise ValueError("mode must be either 'both', 'bars' or 'line'")

        return self

    def color_by(self, column_name: str) -> hist:
        """
        Set the color for the plot.
        """
        if not isinstance(self.df, pd.DataFrame):
            raise ValueError("color_by() can only be used with a dataframe as data source")

        self.main_categories = set_main_categories(self.df, column_name, self.main_categories)
        self.z = column_name

        return self

    def focus_on(self, category: Union[str, list]) -> hist:
        """
        Set the main category for the plot.

        """

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

    def show(self) -> None:

        plt.rcParams.update(self.rcParams)

        if self.z != "":
            categories = self.df[self.z].unique().tolist()
            if len(categories) == 0:
                raise ValueError("No categories found: Length of categories is 0")
        else:
            categories = []

        if len(categories) <= 1:
            color = self.colors["1cat"]
            plt.plot(self.df[self.x], self.df[self.y], color=color, **self.style["line_style"])
            plt.scatter(
                self.df[self.x], self.df[self.y], color=color, **self.style["scatter_style"], marker="s"
            )

        else:
            colors = self.colors["ncats"]

            for category in categories:

                if category not in self.main_categories:

                    x_axis = self.df[self.x][self.df[self.z] == category]
                    y_axis = self.df[self.y][self.df[self.z] == category]

                    if self.mode in ["line", "both"]:

                        plt.plot(
                            x_axis,
                            y_axis,
                            color=self.colors["grayed"],
                            **self.style["lineshadow_style"],
                        )

                    else:

                        plt.scatter(
                            x_axis,
                            y_axis,
                            color=self.colors["grayed"],
                            **self.style["scattershadow_style"],
                        )

            for i, category in enumerate(self.main_categories):

                if len(self.main_categories) == 1:
                    color = self.colors["1cat"]
                else:
                    color = colors[i % len(colors)]

                x_axis = self.df[self.x][self.df[self.z] == category]
                y_axis = self.df[self.y][self.df[self.z] == category]

                if self.mode in ["line", "both"]:
                    plt.plot(x_axis, y_axis, color=color, **self.style["line_style"])
                if self.mode in ["scatter", "both"]:
                    plt.scatter(x_axis, y_axis, color=color, **self.style["scatter_style"])

        plt.ylabel(**self.styleParams["ylabel"])
        plt.xlabel(**self.styleParams["xlabel"])

        # plt.title(**PARAMS["title"])

        # Dirty Trick to extend the plot to the right in Jupyter notebooks
        plt.text(1, 1.09, "t", transform=plt.gcf().transFigure, color=self.rcParams["figure.facecolor"])
        plt.text(-0.05, -0.1, "t", transform=plt.gcf().transFigure, color=self.rcParams["figure.facecolor"])

        if "text" in self.styleParams["title"]:
            plt.annotate(**self.styleParams["title"])

        if "text" in self.styleParams["subtitle"]:
            plt.annotate(**self.styleParams["subtitle"])

        plt.xticks(**self.styleParams["xticks"])
        plt.yticks(**self.styleParams["yticks"])

        plt.show()
