"""Tests for the cleaning module"""
import pandas as pd
from unittest import mock
from pathlib import Path

from life_expectancy.main import main
from life_expectancy.data_loading import load_data, save_data
from life_expectancy.data_cleaning import clean_data

PROJECT_DIR = Path(__file__).parent.parent
FILE_PATH = f"{PROJECT_DIR}/data/eu_life_expectancy_raw.tsv"

def test_main(pt_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""

    pt_life_expectancy_actual = main()

    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )

def test_load_data(eu_life_expectancy_raw):
    """Test for the loading data function"""

    dataframe = load_data(FILE_PATH, "\t")
    pd.testing.assert_frame_equal(
        dataframe, eu_life_expectancy_raw
    )

@mock.patch("pandas.DataFrame.to_csv")
def test_save_data(to_csv, pt_life_expectancy_expected):
    """Test for the saving data function"""

    save_data(pt_life_expectancy_expected, FILE_PATH)
    to_csv.assert_called_with(
        FILE_PATH, index=False
    )

def test_clean_data(eu_life_expectancy_raw, pt_life_expectancy_expected):
    """Test for the cleaning function"""

    dataframe = clean_data(eu_life_expectancy_raw, "PT")
    pd.testing.assert_frame_equal(
        dataframe, pt_life_expectancy_expected
    )