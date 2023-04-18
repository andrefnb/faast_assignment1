"""Tests for the cleaning module"""
from unittest import mock
from pathlib import Path
import pandas as pd

from life_expectancy.data_cleaning import clean_data

def test_clean_data(eu_life_expectancy_raw, pt_life_expectancy_expected):
    """Test for the cleaning function"""

    dataframe = clean_data(eu_life_expectancy_raw, "PT")
    pd.testing.assert_frame_equal(
        dataframe, pt_life_expectancy_expected
    )
