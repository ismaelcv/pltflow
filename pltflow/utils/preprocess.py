import pandas as pd


def set_main_categories(df: pd.DataFrame, column_name: str, main_categories: list) -> list:
    """
    Set the color for the plot.

    """

    if column_name not in df.columns:
        raise ValueError(f"{column_name} not in dataframe")

    if main_categories == []:
        main_categories = list(df[column_name].unique())

    available_values = list(df.loc[df[column_name].isin(main_categories), column_name].value_counts().index)

    if len(main_categories) > 20:
        print(
            f"Posible categories to .focus_on()  {available_values[:20]} and {len(main_categories) - 20} more"
        )
    else:
        print(f"Possible categories to .focus_on() {available_values}")

    return main_categories
