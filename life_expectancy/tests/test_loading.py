"""Tests for the loading/saving module"""
from unittest import mock
import pandas as pd

from life_expectancy.data_loading import load_data, save_data
from life_expectancy.loading_strategy import ConcreteStrategyCSV, ConcreteStrategyCompactedJSON
from . import FIXTURES_DIR

FILE_CSV_PATH = FIXTURES_DIR / "eu_life_expectancy_raw.tsv"
FILE_COMPACTED_JSON_PATH = FIXTURES_DIR / "eurostat_life_expect.zip"

def test_load_data_csv(eu_life_expectancy_raw_csv):
    """Test for the loading data function"""

    strategy = ConcreteStrategyCSV()
    dataframe = load_data(strategy, FILE_CSV_PATH, "\t")
    pd.testing.assert_frame_equal(
        dataframe, eu_life_expectancy_raw_csv
    )

def test_load_data_compacted_json(eu_life_expectancy_raw_json):
    """Test for the loading data function"""

    strategy = ConcreteStrategyCompactedJSON()
    dataframe = load_data(strategy, FILE_COMPACTED_JSON_PATH)
    pd.testing.assert_frame_equal(
        dataframe, eu_life_expectancy_raw_json
    )

@mock.patch("life_expectancy.data_loading.pd.DataFrame.to_csv")
def test_save_data(to_csv, pt_life_expectancy_expected):
    """Test for the saving data function"""

    save_data(pt_life_expectancy_expected, FILE_CSV_PATH)
    to_csv.assert_called_with(
        FILE_CSV_PATH, index=False
    )
