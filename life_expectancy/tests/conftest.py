"""Pytest configuration file"""
from pathlib import Path
import pytest
import pandas as pd

from . import FIXTURES_DIR, OUTPUT_DIR

PROJECT_DIR = Path(__file__).parent.parent
EU_RAW_FILE_PATH = FIXTURES_DIR / "eu_life_expectancy_raw.tsv"
PT_EXPECTED_FILE_PATH = FIXTURES_DIR / "pt_life_expectancy_expected.csv"

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
    dataframe = pd.read_csv(EU_RAW_FILE_PATH, sep = "\t")
    return dataframe

@pytest.fixture(scope="session")
def pt_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to create the filtered expectancy dataframe"""
    dataframe = pd.read_csv(PT_EXPECTED_FILE_PATH)
    return dataframe
