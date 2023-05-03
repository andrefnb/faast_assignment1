"""Tests for the main module"""
from unittest import mock
import pandas as pd
from life_expectancy.region import Region

from life_expectancy.main import main
from . import OUTPUT_DIR

FILE_PATH = OUTPUT_DIR / "eu_life_expectancy_raw.tsv"
SAVE_PATH = OUTPUT_DIR / "pt_life_expectancy.csv"

@mock.patch("life_expectancy.main.load_data")
@mock.patch("life_expectancy.main.clean_data")
@mock.patch("life_expectancy.main.save_data")
def test_main(
    mock_save_data,
    mock_clean_data,
    mock_load_data,
    pt_life_expectancy_expected,
    eu_life_expectancy_raw
    ):
    """Run the main function and compare the output to the expected output"""

    mock_load_data.return_value = eu_life_expectancy_raw
    mock_clean_data.return_value = pt_life_expectancy_expected

    pt_life_expectancy_actual = main()

    mock_load_data.assert_called_once_with(mock.ANY, FILE_PATH, '\t')
    mock_clean_data.assert_called_once_with(eu_life_expectancy_raw, Region.PT)
    mock_save_data.assert_called_once_with(pt_life_expectancy_expected, SAVE_PATH)

    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )
