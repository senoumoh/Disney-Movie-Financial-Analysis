import pandas as pd


def merge_and_clean(character_df, gross_df):
    """
    This function cleans and merges the Disney character and gross dataframes.

    Parameters
    ----------
    character_df: pandas.core.frame.DataFrame
                The Disney character dataframe.
    gross_df: pandas.core.frame.DataFrame
                The Disney gross dataframe.

    Returns
    -------
    result_df: pandas.core.frame.DataFrame
                The cleaned and merged dataframe

    Examples
    --------
    >>> merge_and_clean(character_df, gross_df)
    """

    if not isinstance(character_df, pd.DataFrame):
        raise TypeError("The character_df argument is not of type DataFrame")

    if not isinstance(gross_df, pd.DataFrame):
        raise TypeError("The gross_df argument is not of type DataFrame")

    result_df = pd.merge(character_df, gross_df, on="movie_title", how="right")
    result_df = (
        result_df.assign(
            total_gross=result_df["total_gross"]
            .str.replace("$", "")
            .str.replace(",", "")
            .astype("int64"),
            inflation_adjusted_gross=result_df["inflation_adjusted_gross"]
            .str.replace("$", "")
            .str.replace(",", "")
            .astype("int64"),
            is_musical=~(result_df["song"].isna() | (result_df["song"] == "No data")),
            release_date=result_df["release_date_x"].fillna(
                result_df["release_date_y"]
            ),
        )
        .fillna("No data")
        .drop(columns=["release_date_x", "release_date_y"])
    )

    result_df["release_date"] = pd.to_datetime(
        result_df["release_date"], format="mixed", errors="coerce"
    )

    return result_df


def calculate_yearly_averages(cleaned_df):
    """
    Calculates the average inflation-adjusted gross per year,
    separated by musical and non-musical films.

    Parameters
    ----------
    cleaned_df: pandas.core.frame.DataFrame
                The cleaned and merged Disney dataframe.

    Returns
    -------
    result_df: pandas.core.frame.DataFrame
                The dataframed grouped by release year and is_musical

    Examples
    --------
    >>> calculate_yearly_averages(cleaned_df)
    """

    if not isinstance(cleaned_df, pd.DataFrame):
        raise TypeError("The cleaned_df argument is not of type DataFrame")

    trend_df = cleaned_df.copy()

    trend_df["release_year"] = pd.to_datetime(trend_df["release_date"]).dt.year

    yearly_summary = (
        trend_df.groupby(["release_year", "is_musical"])["inflation_adjusted_gross"]
        .mean()
        .reset_index()
    )

    yearly_summary = yearly_summary.rename(
        columns={"inflation_adjusted_gross": "average_gross"}
    )

    return yearly_summary
