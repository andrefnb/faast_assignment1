"""
Main script for life_expectancy module
"""

from pathlib import Path
import pandas as pd
from life_expectancy.data_loading import load_data, save_data
from life_expectancy.data_cleaning import clean_data
from life_expectancy.loading_strategy import ConcreteLoadingStrategyCSV, ConcreteLoadingStrategyCompactedJSON
from life_expectancy.cleaning_strategy import ConcreteCleaningStrategyCSV, ConcreteCleaningStrategyCompactedJSON
from life_expectancy.region import Region

PROJECT_DIR = Path(__file__).parent
FILE_CSV_PATH = PROJECT_DIR / "data" / "eu_life_expectancy_raw.tsv"
SAVE_CSV_PATH = PROJECT_DIR / "data" / "pt_life_expectancy.csv"
FILE_COMPACTED_JSON_PATH = PROJECT_DIR / "data" / "eurostat_life_expect.zip"
SAVE_COMPACTED_JSON_PATH = PROJECT_DIR / "data" / "pt_life_expectancy_json.csv"

def main_csv(country: Region = Region.PT) -> pd.DataFrame:
    """Main function using the csv format."""

    loading_strategy = ConcreteLoadingStrategyCSV()
    dataframe = load_data(loading_strategy, FILE_CSV_PATH, '\t')
    cleaning_strategy = ConcreteCleaningStrategyCSV()
    cleaned_df = clean_data(cleaning_strategy, dataframe, country)

    save_data(cleaned_df, SAVE_CSV_PATH)

    return cleaned_df

def main_compacted_json(country: Region = Region.PT) -> pd.DataFrame:
    """Main function using the compacted json format."""

    loading_strategy = ConcreteLoadingStrategyCompactedJSON()
    dataframe = load_data(loading_strategy, FILE_COMPACTED_JSON_PATH)
    cleaning_strategy = ConcreteCleaningStrategyCompactedJSON()
    cleaned_df = clean_data(cleaning_strategy, dataframe, country)

    save_data(cleaned_df, SAVE_COMPACTED_JSON_PATH)

    return cleaned_df
