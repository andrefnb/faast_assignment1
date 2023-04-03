"""Pytest configuration file"""
from pathlib import Path
import pytest
import pandas as pd

from life_expectancy.data_cleaning import clean_data

from . import FIXTURES_DIR, OUTPUT_DIR

PROJECT_DIR = Path(__file__).parent.parent
FILE_PATH = f"{PROJECT_DIR}/data/eu_life_expectancy_raw.tsv"

@pytest.fixture(autouse=True)
def run_before_and_after_tests() -> None:
    """Fixture to execute commands before and after a test is run"""
    # Setup: fill with any logic you want

    yield # this is where the testing happens

    # Teardown : fill with any logic you want
    file_path = OUTPUT_DIR / "pt_life_expectancy.csv"
    file_path.unlink(missing_ok=True)

@pytest.fixture(scope="session")
def eu_life_expectancy_raw() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    dataframe = pd.read_csv(FILE_PATH, sep = "\t")
    dataframe.to_csv(FIXTURES_DIR / "eu_life_expectancy_raw.tsv", sep = "\t",index = False)
    return dataframe

@pytest.fixture(scope="session")
def pt_life_expectancy_expected(eu_life_expectancy_raw) -> pd.DataFrame:
    """Fixture to create the filtered expectancy dataframe"""
    dataframe = clean_data(eu_life_expectancy_raw, "PT")
    dataframe.to_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv", index = False)
    return dataframe
