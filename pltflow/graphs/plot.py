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
            "single": {"palette": [self.colors["hist"][-1]]},
            "multiple": {"palette": self.create_palette(categories), "hue": self.z},
        }  # type: dict

        common_params = {
            "data": self.df,
            "x": self.x,
            "y": self.y,
            "legend": False,
        }

        if self.mode == "line":
            sns.lineplot(
                **common_params,
                **color_params[mode],
                **self.styleParams[self.mode],
            )
        if self.mode == "scatter":
            sns.scatterplot(
                **common_params,
                **color_params[mode],
                **self.styleParams[self.mode],
            )

        if len(categories) > 1:
            patches = create_legend_patches(color_params[mode]["palette"])
            plt.legend(handles=patches)

        self.display_chart_annotations()
        self.plot_padding((1.02, 1.2), (-0.01, -0.0))

        plt.show()


class scatter(line):
    ...
