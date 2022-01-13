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
    "styleParams": {
        "xticks": {"fontsize": 11, "fontweight": "bold"},
        "yticks": {"fontsize": 11, "fontweight": "bold"},
        "ylabel": {"fontsize": 12, "fontweight": "bold"},
        "xlabel": {"fontsize": 12, "fontweight": "bold"},
        "title": {
            "fontsize": 18,
            "color": "white",
            "fontweight": "bold",
            "xy": (0.00, 1.22),
            "xycoords": "axes fraction",
        },
        "subtitle": {
            "color": "white",
            "fontsize": 14,
            "xy": (0.00, 1.14),
            "xycoords": "axes fraction",
        },
        "scatter_style": {"s": 30},
        "line_style": {"linewidth": 2},
        "hist": {
            "kde": {"linewidth": 0.1, "fill": True, "alpha": 0.7},
            "hist": {"linewidth": 0.1, "bins": 40, "alpha": 0.7},
        },
    },
    "colors": {
        "plot": {"1cat": "#aed7eb", "ncats": plt_tab_colors, "grayed": "#566a6b"},
        "hist": {"1cat": "white", "ncats": plt_tab_colors, "grayed": "#566a6b"},
    },
}
