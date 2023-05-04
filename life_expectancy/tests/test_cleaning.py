"""Tests for the cleaning module"""
import pandas as pd
from life_expectancy.region import Region

from life_expectancy.data_cleaning import clean_data
from life_expectancy.cleaning_strategy import ConcreteCleaningStrategyCSV, ConcreteCleaningStrategyCompactedJSON

def test_clean_data_csv(eu_life_expectancy_raw_csv, pt_life_expectancy_expected):
    """Test for the cleaning function with the csv format"""

    strategy = ConcreteCleaningStrategyCSV()
    dataframe = clean_data(strategy, eu_life_expectancy_raw_csv, Region.PT)
    pd.testing.assert_frame_equal(
        dataframe, pt_life_expectancy_expected
    )

def test_clean_data_json(eu_life_expectancy_raw_json, pt_life_expectancy_expected):
    """Test for the cleaning function with the json format"""

    strategy = ConcreteCleaningStrategyCompactedJSON()
    dataframe = clean_data(strategy, eu_life_expectancy_raw_json, Region.PT)
    pd.testing.assert_frame_equal(
        dataframe, pt_life_expectancy_expected
    )
