from pltflow.utils.colors import plt_tab_colors

MAIN_FONT = "monofur for powerline"

style = {
    "rcParams": {
        # Background color
        "axes.facecolor": "#F3F0E0",
        "figure.facecolor": "#F3F0E0",
        # Labels settings
        "axes.labelcolor": "black",
        "axes.labelsize": 20,
        "axes.labelpad": 25,
        # XY line axis color
        "axes.edgecolor": "black",
        # XY line width
        "axes.linewidth": 0.5,
        # XY line remove top/right
        "axes.spines.right": False,
        "axes.spines.top": False,
        # Change xy axis color
        "xtick.color": "black",
        "ytick.color": "black",
        "xtick.major.size": 7,
        "xtick.major.width": 1,
        "ytick.major.size": 7,
        "ytick.major.width": 1,
        # Y grid
        "axes.grid": True,
        "axes.grid.axis": "both",
        "grid.linestyle": "--",
        "grid.linewidth": 1,
        "grid.alpha": 0.2,
        "grid.color": "#9e9d9d",
        # Savefig properties
        "savefig.facecolor": "white",
        "savefig.edgecolor": "white",
    },
    "lineshadow_style": {
        "linewidth": 1,
    },
    "scattershadow_style": {
        "s": 20,
    },
    "scatter_style": {
        "s": 20,
    },
    "line_style": {
        "linewidth": 1.2,
    },
    "styleParams": {
        "xticks": {"fontsize": 13, "fontweight": "normal", "fontname": MAIN_FONT},
        "yticks": {"fontsize": 13, "fontweight": "normal", "fontname": MAIN_FONT},
        "ylabel": {"fontsize": 17, "fontname": MAIN_FONT, "labelpad": 14},
        "xlabel": {"fontsize": 17, "fontname": MAIN_FONT, "labelpad": 14},
        "title": {
            "fontsize": 20,
            "fontweight": "bold",
            "xy": (0.00, 1.17),
            "xycoords": "axes fraction",
            "fontname": MAIN_FONT,
        },
        "subtitle": {
            "fontsize": 16,
            "color": "#696969",
            "xy": (0.00, 1.09),
            "xycoords": "axes fraction",
            "fontname": "monofur for powerline",
        },
    },
    "colors": {"1cat": "#244796", "ncats": plt_tab_colors, "grayed": "#9c9b92"},
}
