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

    def __init__(
        self,
        data: Union[pd.DataFrame, list, np.ndarray, pd.Series],
        x: str = "",
        style: str = "base",
        mode: str = "hist",
        **kwargs: dict,
    ) -> None:

        # This function includes initialization common for all the clases
        self.initialize_plot_parameters(mode, style, kwargs)

        # Initialize the plot for the specific class
        self.prepare_data(data, x)

    def prepare_data(
        self,
        data: Union[pd.DataFrame, list, np.ndarray, pd.Series],
        x: str,
        y: str = "",
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

    def show(self) -> None:

        plt.rcParams.update(self.rcParams)

        categories = self.get_hue_categories()

        height = self.rcParams["figure.figsize"][1]
        aspect = self.rcParams["figure.figsize"][0] / height

        mode = "single" if len(categories) <= 1 else "multiple"

        params = {
            "single": {"palette": [self.colors["hist"][-1]]},
            "multiple": {"palette": self.create_palette(categories), "hue": self.z},
        }  # type: dict

        sns.displot(
            self.df,
            x=self.x,
            height=height,
            aspect=aspect,
            kind=self.mode,
            legend=False,
            **params[mode],
            **self.styleParams["hist"][self.mode],
        )

        if len(categories) > 1:
            patches = create_legend_patches(params[mode]["palette"])
            plt.legend(handles=patches)

        self.display_chart_annotations()
        self.plot_padding((1.02, 1.2), (-0.01, -0.0))

        plt.show()


class hist_tabular(hist):

    """
    Generic class to genererate an histogram in style
    """

    def __init__(
        self,
        data: pd.DataFrame,
        x: Union[str, list],
        style: str = "base",
        mode: str = "hist",
        **kwargs: dict,
    ) -> None:

        # This function includes initialization common for all the clases
        self.initialize_plot_parameters(mode, style, kwargs)

        # Initialize the plot for the specific class
        self.prepare_data(data, x)

    def prepare_data(
        self,
        data: pd.DataFrame,
        x: Union[str, list],
        y: str = "",
    ) -> None:
        """
        This parameters are set for the case of scatterplots.
        In this mode the only valid input is a dataframe
        """

        if isinstance(x, list):
            self.df = data.loc[:, x].melt(var_name="_key", value_name="_value")

            self.x = "_value"
            self.color_by("_key")
            self.set_xlabel("")

        else:
            self.df = pd.DataFrame({"x": data[x]})
            self.x = "x"
            self.set_xlabel("")

        self.y = ""
        self.set_ylabel(self.y)
