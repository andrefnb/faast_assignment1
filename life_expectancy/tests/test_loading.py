"""Tests for the loading/saving module"""
from unittest import mock
import pandas as pd

from life_expectancy.data_loading import load_data, save_data
from . import FIXTURES_DIR

FILE_PATH = FIXTURES_DIR / "eu_life_expectancy_raw.tsv"

def test_load_data(eu_life_expectancy_raw):
    """Test for the loading data function"""

    dataframe = load_data(FILE_PATH, "\t")
    pd.testing.assert_frame_equal(
        dataframe, eu_life_expectancy_raw
    )

@mock.patch("life_expectancy.data_loading.pd.DataFrame.to_csv")
def test_save_data(to_csv, pt_life_expectancy_expected):
    """Test for the saving data function"""

    save_data(pt_life_expectancy_expected, FILE_PATH)
    to_csv.assert_called_with(
        FILE_PATH, index=False
    )
