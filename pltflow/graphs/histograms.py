from __future__ import annotations  # To be able to do type annotations

from typing import Optional, Union

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

from pltflow.graphs.base_chart import chart
from pltflow.utils.data_checks import check_array_is_numeric


class hist(chart):

    """
    Generic class to genererate an histogram in style
    """

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
        self.set_title("")
        self.set_subtitle("")

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

        # color = self.colors["1cat"]

        height = self.rcParams["figure.figsize"][1]
        aspect = self.rcParams["figure.figsize"][0] / height

        if self.mode in ["kde", "default", "hist"]:

            sns.displot(
                self.df,
                x=self.x,
                height=height,
                aspect=aspect,
                kind=self.mode,
                bins=40,
            )  # ,", color="lightgray", alpha=0.4, fill=True, linewidth=0)

    def show(self) -> None:

        plt.rcParams.update(self.rcParams)

        categories = self.get_hue_categories()

        if len(categories) <= 1:
            self.plot_one_category()

        # else:
        #     self.plot_grayed_categories(categories)
        #     self.plot_multiple_categories(categories)

        self.display_chart_annotations()
        self.plot_padding((1.02, 1.2), (-0.01, -0.0))

        plt.show()
