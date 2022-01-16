from __future__ import annotations

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

from pltflow.graphs.base_chart import chart


class line(chart):

    """
    Generic class to genererate a plt graph
    """

    def __init__(
        self,
        data: pd.DataFrame,
        x: str = "",
        y: str = "",
        style: str = "base",
        markers: bool = True,
        **kwargs: dict,
    ) -> None:

        self.markers = markers

        # This function includes initialization common for all the clases
        self.initialize_plot_parameters(style, kwargs)

        # Initialize the plot for the specific class
        self.prepare_data(data, x, y)

    def plot_multiple_categories(self) -> None:

        colors = self.colors["ncats"]

        for i, category in enumerate(self.main_categories):

            if len(self.main_categories) == 1:
                color = self.colors["1cat"]
            else:
                color = colors[i % len(colors)]

            x_axis = self.df[self.x][self.df[self.z] == category]
            y_axis = self.df[self.y][self.df[self.z] == category]

            if self.mode in ["line", "default"]:
                plt.plot(x_axis, y_axis, color=color, **self.styleParams["line_style"])
            if self.mode in ["scatter", "default"]:
                plt.scatter(x_axis, y_axis, color=color, **self.styleParams["scatter_style"])

    # def plot_one_category(self) -> None:

    #     color = self.colors[0]

    #     if self.mode in ["line", "default"]:
    #         plt.plot(self.df[self.x], self.df[self.y], color=color, **self.styleParams["line_style"])
    #     if self.mode in ["scatter", "default"]:
    #         plt.scatter(self.df[self.x], self.df[self.y], color=color, **self.styleParams["scatter_style"])

    # def plot_grayed_categories(self, categories: list) -> None:

    #     for category in categories:

    #         if category not in self.main_categories:

    #             x_axis = self.df[self.x][self.df[self.z] == category]
    #             y_axis = self.df[self.y][self.df[self.z] == category]

    #             if self.mode in ["line", "default"]:

    #                 sns.lineplot()

    #                 plt.plot(
    #                     x_axis,
    #                     y_axis,
    #                     color=self.colors[-1],
    #                     **self.styleParams["lineshadow_style"],
    #                 )

    #             else:

    #                 plt.scatter(
    #                     x_axis,
    #                     y_axis,
    #                     color=self.colors[-1],
    #                     **self.styleParams["scattershadow_style"],
    #                 )

    def show(self) -> None:

        plt.rcParams.update(self.rcParams)

        categories = self.get_hue_categories()

        if len(categories) <= 1:
            self.plot_one_category()

        else:
            self.plot_grayed_categories(categories)
            self.plot_multiple_categories()

        self.display_chart_annotations()
        self.plot_padding((1, 1.1), (-0.05, -0.1))

        plt.show()
