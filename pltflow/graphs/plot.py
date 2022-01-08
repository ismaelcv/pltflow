from __future__ import annotations

from typing import Optional, Union

import pandas as pd
from matplotlib import pyplot as plt

from pltflow.utils.utils import load_styles


class plot:

    """
    Generic class to genererate a plt graph
    """

    def __init__(self, df: pd.DataFrame, x: str, y: str, style: str = "base", mode: str = "both") -> None:

        self.STYLES = load_styles()

        plt.rcParams.update(plt.rcParamsDefault)

        self.df = df
        self.x = x
        self.y = y
        self._set_mode(mode)
        self._set_style(style)
        self.set_xlabel(self.x)
        self.set_ylabel(self.y)
        self.set_figsize()
        self.z = ""  # type: str
        self.main_categories = []  # type: list
        self.notes = []  # type: list

    def color_by(self, column_name: str) -> plot:
        """
        Set the color for the plot.

        """

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

    def _set_mode(self, mode: str) -> None:

        if mode in ["both", "scatter", "line"]:
            self.mode = mode
        else:
            raise ValueError("mode must be either 'both', 'scatter' or 'line'")

    def focus_on(self, category: Union[str, list]) -> plot:
        """
        Set the main category for the plot.

        """

        if self.z == "":
            raise ValueError(
                """
                No column to split on selected (z)
                Please select a column with .color_by("column_name ")
                """
            )

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

    def _set_style(self, style: str) -> plot:

        if style in self.STYLES:
            self.style = self.STYLES[style]
            self.styleParams = self.STYLES[style]["styleParams"]
            self.rcParams = self.STYLES[style]["rcParams"]
            self.colors = self.STYLES[style]["colors"]

        else:
            raise ValueError(f"{style} is not a valid style")

        return self

    def set_yticks(self, positions: list, **kwargs: dict) -> plot:
        self.styleParams["yticks"] = {**self.styleParams["yticks"], **{"ticks": positions}, **kwargs}
        return self

    def set_xticks(self, positions: list, **kwargs: dict) -> plot:
        self.styleParams["xticks"] = {**self.styleParams["xticks"], **{"ticks": positions}, **kwargs}
        return self

    def set_ylabel(self, label: str, **kwargs: dict) -> plot:
        self.styleParams["ylabel"] = {**self.styleParams["ylabel"], **{"ylabel": label}, **kwargs}
        return self

    def set_xlabel(self, label: str, **kwargs: dict) -> plot:
        self.styleParams["xlabel"] = {**self.styleParams["xlabel"], **{"xlabel": label}, **kwargs}
        return self

    def set_title(self, title: str, **kwargs: dict) -> plot:

        self.styleParams["title"] = {**self.styleParams["title"], **{"text": title}, **kwargs}

        return self

    def set_subtitle(self, subtitle: str) -> plot:
        self.styleParams["subtitle"]["text"] = subtitle

        return self

    def set_figsize(self, w: int = 9, h: int = 4) -> plot:
        if w > 0 and h > 0:
            self.rcParams["figure.figsize"] = (w, h)

        else:
            raise ValueError("w and h must be greater than 0")
        return self

    def _set_styleParams(self, params: dict) -> None:
        """
        Set parameters for the plot.

        """
        for key, value in params.items():
            if key in self.styleParams:
                self.styleParams[key] = value

    def add_note(
        self,
        text: str,
        x: float,
        y: Optional[float] = None,
        category: Optional[str] = None,
        **kwargs: dict,
    ) -> plot:

        if text is None:
            raise ValueError("An input text is required")

        if x is not None and y is not None:
            self.notes.append(
                [
                    {
                        "text": text,
                        "xy": (x, y),
                        "xytext": (x + 5, y + 10),
                        "arrowprops": {"arrowstyle": "->", "connectionstyle": "angle3,angleA=0,angleB=-90"},
                        "size": 15,
                    },
                    kwargs,
                ]
            )
        if category is not None and category not in self.main_categories:
            raise ValueError(
                f"{category} not in main categories. Available categories f{self.main_categories}"
            )

        if category is not None and self.z == "":
            raise ValueError(
                """
                It is not possible to specify a category on a single colored plot.
                Use color_by() to be able to specify a category
                """
            )

        if y is None:

            self._check_is_numeric(self.x)

            if category is None and len(self.main_categories) > 1:
                raise ValueError(
                    f"""
                Error: Ambiguity where to place the note You need to specify a category.
                Available categories {self.main_categories}"
                """
                )

            if category is None and self.z == "":
                selection = self.df[self.x]
                index_closest_x = abs(selection.sort_values() - x).sort_values().index[0]

            elif category is not None:
                selection = self.df[self.df[self.z] == category][self.x]
                index_closest_x = abs(selection.sort_values() - x).sort_values().index[0]

            closest_x = selection.loc[index_closest_x]
            y = self.df[self.df[self.x] == closest_x][self.y].iat[0]

            self.notes.append(
                [
                    {
                        "text": text,
                        "xy": (closest_x, y),
                        "xytext": (closest_x + 5, y + 10),
                        "arrowprops": {"arrowstyle": "->", "connectionstyle": "angle3,angleA=0,angleB=-90"},
                        "size": 15,
                    },
                    kwargs,
                ]
            )

        return self

    def _check_is_numeric(self, column: str) -> None:
        try:
            self.df[column].astype("float64")
        except ValueError:
            print(
                f"""
                {column} is not a numerical python type.
                Notes based on only one axis can only be perfom on numerical columns")
                """
            )

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
