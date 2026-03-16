import pandas as pd
import pytest
from disney_utils import merge_and_clean, calculate_yearly_averages


def test_merge_and_clean_valid():
    """
    Test that the merge_and_clean function works as expected.
    """
    mock_character = pd.DataFrame(
        {
            "movie_title": ["Snow White and the Seven Dwarfs", "Pinocchio", "Fantasia"],
            "release_date": [
                "December 21, 1937",
                "February 7, 1940",
                "November 13, 1940",
            ],
            "hero": ["Snow White", "Pinocchio", ""],
            "villian": ["Evil Queen", "Stromboli", "Chernabog"],
            "song": ["Some Day My Prince Will Come", "When You Wish upon a Star", ""],
        }
    )

    mock_gross = pd.DataFrame(
        {
            "movie_title": ["Snow White and the Seven Dwarfs", "Pinocchio", "Fantasia"],
            "release_date": ["Dec 21, 1937", "Feb 9, 1940", "Nov 13, 1940"],
            "genre": ["Musical", "Adventure", "Musical"],
            "MPAA_rating": ["G", "G", "G"],
            "total_gross": ["$100,100,100", "$110,100,100", "$200,100,100"],
            "inflation_adjusted_gross": [
                "$100,100,100,000",
                "$110,100,100,100",
                "$200,100,100,200",
            ],
        }
    )

    test_result = merge_and_clean(mock_character, mock_gross)

    assert len(test_result) == 3
    assert "total_gross" in test_result.columns
    assert test_result["total_gross"].iloc[0] == 100100100
    assert test_result["total_gross"].dtype == "int64"


def test_merge_and_clean_exception():
    """
    Test that an exception is raised as expected for invalid dataframes
    """

    with pytest.raises(TypeError):
        merge_and_clean("Something invalid", "Another invalid")


def test_calculate_yearly_averages_exception():
    """
    Test that an exception is raised as expected for invalid dataframes
    """

    with pytest.raises(TypeError):
        calculate_yearly_averages("Something invalid")
