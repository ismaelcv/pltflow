from __future__ import annotations  # To be able to do type annotations

from typing import Union

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

from pltflow.graphs.base_chart import chart
from pltflow.utils.data_checks import check_array_is_numeric
from pltflow.utils.styling import create_legend_patches


class hist(chart):

    """
    Generic class to genererate an histogram in style
    """

    def set_parameters(
        self,
        data: Union[pd.DataFrame, list, np.ndarray, pd.Series],
        x: str,
        y: str,
    ) -> None:
        """
        This parameters are set for the case of scatterplots.
        In this mode the only valid input is a dataframe
        """

        if isinstance(data, pd.DataFrame):
            self.df = data
            if x in self.df.columns:
                self.x = x
                self.set_xlabel(x)
            else:
                raise ValueError("X should be a valid column name")
        else:
            check_array_is_numeric(data)
            self.df = pd.DataFrame({"x": data})
            self.x = "x"
            self.set_xlabel("")

        self.y = ""
        self.set_ylabel(self.y)

    def _set_mode(self, mode: str) -> None:
        """
        default: "hist"
        kde: "Kernell density estimator"
        """

        if mode in ["default", "hist"]:
            mode = "hist"
            self.set_ylabel("frecuency")
        elif mode in ["kde"]:
            self.set_ylabel("density")
        else:
            raise ValueError("mode must be either 'default' (hist)' or 'kde'")

        self.mode = mode

    def plot_one_category(self) -> None:
        height = self.rcParams["figure.figsize"][1]
        aspect = self.rcParams["figure.figsize"][0] / height
        color = self.colors["hist"]["1cat"]

        sns.displot(
            self.df,
            x=self.x,
            height=height,
            aspect=aspect,
            kind=self.mode,
            color=color,
            **self.styleParams["hist"][self.mode],
        )

    def plot_multiple_categories(self, categories: list) -> None:

        colors = self.colors["hist"]["ncats"]
        height = self.rcParams["figure.figsize"][1]
        aspect = self.rcParams["figure.figsize"][0] / height

        i = 0
        color_assigment = []

        for category in categories:
            if category in self.main_categories:
                color_assigment += [colors[i % len(colors)]]
                i += 1
            else:
                color_assigment += [self.colors["hist"]["grayed"]]

        palette = dict(zip(categories, color_assigment))

        sns.displot(
            self.df,
            x=self.x,
            hue=self.z,
            height=height,
            aspect=aspect,
            kind=self.mode,
            palette=palette,
            legend=False,
            **self.styleParams["hist"][self.mode],
        )

        patches = create_legend_patches(palette)
        plt.legend(handles=patches, loc="best")

    def show(self) -> None:

        plt.rcParams.update(self.rcParams)

        categories = self.get_hue_categories()

        if len(categories) <= 1:
            self.plot_one_category()

        else:
            self.plot_multiple_categories(categories)

        self.display_chart_annotations()
        self.plot_padding((1.02, 1.2), (-0.01, -0.0))

        plt.show()
