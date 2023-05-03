"""Tests for the cleaning module"""
import pandas as pd
from life_expectancy.region import Region

from life_expectancy.data_cleaning import clean_data

def test_clean_data(eu_life_expectancy_raw_csv, pt_life_expectancy_expected):
    """Test for the cleaning function"""

    dataframe = clean_data(eu_life_expectancy_raw_csv, Region.PT)
    pd.testing.assert_frame_equal(
        dataframe, pt_life_expectancy_expected
    )
