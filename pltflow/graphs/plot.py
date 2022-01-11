from __future__ import annotations

from matplotlib import pyplot as plt

from pltflow.graphs.base_chart import chart


class plot(chart):

    """
    Generic class to genererate a plt graph
    """

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
            plt.plot(self.df[self.x], self.df[self.y], color=color, **self.styleParams["line_style"])
            plt.scatter(
                self.df[self.x], self.df[self.y], color=color, **self.styleParams["scatter_style"], marker="s"
            )

        else:
            colors = self.colors["ncats"]

            for category in categories:

                if category not in self.main_categories:

                    x_axis = self.df[self.x][self.df[self.z] == category]
                    y_axis = self.df[self.y][self.df[self.z] == category]

                    if self.mode in ["line", "default"]:

                        plt.plot(
                            x_axis,
                            y_axis,
                            color=self.colors["grayed"],
                            **self.styleParams["lineshadow_style"],
                        )

                    else:

                        plt.scatter(
                            x_axis,
                            y_axis,
                            color=self.colors["grayed"],
                            **self.styleParams["scattershadow_style"],
                        )

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
