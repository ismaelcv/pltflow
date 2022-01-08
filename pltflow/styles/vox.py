from pltflow.utils.colors import plt_tab_colors

style = {
    "rcParams": {
        # Background color
        "axes.facecolor": "#3a4849",
        "figure.facecolor": "#3a4849",
        # Labels settings
        "axes.labelcolor": "white",
        "axes.labelsize": 20,
        "axes.labelpad": 25,
        # XY line axis color
        "axes.edgecolor": "#62737c",
        # XY line width
        "axes.linewidth": 2,
        # XY line remove top/right
        "axes.spines.right": False,
        "axes.spines.top": False,
        # Change xy axis color
        "xtick.color": "white",
        "ytick.color": "white",
        "xtick.major.size": 0,
        "ytick.major.size": 0,  # Y grid
        "grid.color": "lightgray",
        "grid.alpha": 0.4,
        "axes.grid": False,
        "axes.grid.axis": "y",
        # Savefig properties
        "savefig.facecolor": "black",
        "savefig.edgecolor": "black",
    },
    "scatter_style": {
        "s": 30,
        "marker": "s",
    },
    "line_style": {
        "linewidth": 2,
    },
    "scattershadow_style": {
        "s": 30,
    },
    "lineshadow_style": {
        "linewidth": 2,
    },
    "styleParams": {
        "xticks": {"fontsize": 11, "fontweight": "bold"},
        "yticks": {"fontsize": 11, "fontweight": "bold"},
        "ylabel": {"fontsize": 12, "fontweight": "bold"},
        "xlabel": {"fontsize": 12, "fontweight": "bold"},
        "title": {
            "fontsize": 18,
            "color": "white",
            "fontweight": "bold",
            "xy": (0.00, 1.16),
            "xycoords": "axes fraction",
        },
        "subtitle": {
            "color": "white",
            "fontsize": 14,
            "xy": (0.00, 1.095),
            "xycoords": "axes fraction",
        },
    },
    "colors": {"1cat": "#aed7eb", "ncats": plt_tab_colors, "grayed": "#566a6b"},
}
