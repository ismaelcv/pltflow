from __future__ import annotations

import seaborn as sns
from matplotlib import pyplot as plt

from pltflow.graphs.base_chart import chart
from pltflow.utils.styling import create_legend_patches


class line(chart):

    """
    Generic class to genererate a plt graph
    """

    def show(self) -> None:

        plt.rcParams.update(self.rcParams)

        categories = self.get_hue_categories()

        mode = "single" if len(categories) <= 1 else "multiple"

        color_params = {
            "single": {"palette": [self.colors[self.mode][0]]},
            "multiple": {"palette": self.create_palette(categories), "hue": self.z},
        }  # type: dict

        common_params = {
            "data": self.df,
            "x": self.x,
            "y": self.y,
            "legend": False,
        }

        if self.mode == "line":

            print(color_params[mode])

            sns.lineplot(
                **common_params,
                **color_params[mode],
                **self.styleParams[self.mode],
            )

            if self.markers and self.z != "":

                common_params["data"] = self.df[self.df[self.z].isin(self.main_categories)]

                sns.scatterplot(
                    **common_params,
                    **color_params[mode],
                    s=50,
                    alpha=0.9,
                    linewidth=0,
                    marker="s",
                )

        if self.mode == "scatter":

            print(self.mode, self.styleParams[self.mode])

            sns.scatterplot(
                **common_params,
                **color_params[mode],
                **self.styleParams[self.mode],
            )

        if len(categories) > 1:

            patches = create_legend_patches(
                color_params[mode]["palette"], grayed_color=self.colors[self.mode][-1]
            )

            plt.legend(handles=patches)

        self.display_chart_annotations()
        self.plot_padding((1.02, 1.2), (-0.07, -0.2))

        plt.show()

    #TODO: fix thisssss
    def plot_multiple_categories(self, palette:dict) -> None:

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

class scatter(line):
    ...
