"""Tests for the main module"""
from unittest import mock
import pandas as pd
from life_expectancy.region import Region

from life_expectancy.main import main_csv, main_compacted_json
from . import OUTPUT_DIR

FILE_CSV_PATH = OUTPUT_DIR / "eu_life_expectancy_raw.tsv"
SAVE_CSV_PATH = OUTPUT_DIR / "pt_life_expectancy.csv"
FILE_COMPACTED_JSON_PATH = OUTPUT_DIR / "eurostat_life_expect.zip"
SAVE_JSON_PATH = OUTPUT_DIR / "pt_life_expectancy_json.csv"

@mock.patch("life_expectancy.main.load_data")
@mock.patch("life_expectancy.main.clean_data")
@mock.patch("life_expectancy.main.save_data")
def test_main_csv(
    mock_save_data,
    mock_clean_data,
    mock_load_data,
    pt_life_expectancy_expected,
    eu_life_expectancy_raw_csv
    ):
    """Run the main function and compare the output to the expected output"""

    mock_load_data.return_value = eu_life_expectancy_raw_csv
    mock_clean_data.return_value = pt_life_expectancy_expected

    pt_life_expectancy_actual = main_csv()

    mock_load_data.assert_called_once_with(mock.ANY, FILE_CSV_PATH, '\t')
    mock_clean_data.assert_called_once_with(mock.ANY, eu_life_expectancy_raw_csv, Region.PT)
    mock_save_data.assert_called_once_with(pt_life_expectancy_expected, SAVE_CSV_PATH)

    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )

@mock.patch("life_expectancy.main.load_data")
@mock.patch("life_expectancy.main.clean_data")
@mock.patch("life_expectancy.main.save_data")
def test_main_compacted_json(
    mock_save_data,
    mock_clean_data,
    mock_load_data,
    pt_life_expectancy_expected,
    eu_life_expectancy_raw_json
    ):
    """Run the main function and compare the output to the expected output"""

    mock_load_data.return_value = eu_life_expectancy_raw_json
    mock_clean_data.return_value = pt_life_expectancy_expected

    pt_life_expectancy_actual = main_compacted_json()

    mock_load_data.assert_called_once_with(mock.ANY, FILE_COMPACTED_JSON_PATH)
    mock_clean_data.assert_called_once_with(mock.ANY, eu_life_expectancy_raw_json, Region.PT)
    mock_save_data.assert_called_once_with(pt_life_expectancy_expected, SAVE_JSON_PATH)

    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )
