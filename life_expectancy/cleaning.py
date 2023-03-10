"""
Cleaning script
"""

import re
from pathlib import Path
from typing import List
import pandas as pd
import numpy as np

PROJECT_DIR = Path(__file__).parent
FILE_PATH = f"{PROJECT_DIR}/data/eu_life_expectancy_raw.tsv"
SAVE_PATH = "life_expectancy/data/pt_life_expectancy.csv"
COL_TO_SPLIT = 'unit,sex,age,geo\\time'
SPLITTED_COLS_LIST = ['unit', 'sex', 'age', 'region']



def main(country: str = "PT") -> None: #pragma: no cover
    """Main function."""

    dataframe = load_data(FILE_PATH, '\t')

    cleaned_df = clean_data(dataframe, COL_TO_SPLIT, SPLITTED_COLS_LIST, country)

    save_data(cleaned_df, SAVE_PATH)

def load_data(file_path: str, sep: str = ",") -> pd.DataFrame:
    """Loads a CSV file given a path and separator."""
    return pd.read_csv(file_path, sep=sep)
    
def clean_data(dataframe: pd.DataFrame, col_to_split: str, splitted_cols_list: List[str], country: str) -> pd.DataFrame:
    """Function that will clean, transform and filter (by region, its default being PT) the life_expectancy data."""
    
    # Split first column
    dataframe[splitted_cols_list] = dataframe[col_to_split].str.split(",", expand=True)
    dataframe = dataframe.drop(columns=col_to_split)

    # Unpivot data
    dataframe = pd.melt(dataframe, id_vars=splitted_cols_list, var_name="year", value_name="value")
    
    # Apply some conversions
    dataframe["year"] = pd.to_numeric(dataframe["year"], errors="coerce").astype(int)

    # Apply the str_to_float method and perform data cleaning
    dataframe['value'] = [__str_to_float(val) for val in dataframe["value"]]

    # Remove natural NaNs, but also the coerced invalid values from the previous value conversion
    dataframe.dropna(subset=["value"], inplace=True)

    # Filter by region
    dataframe = dataframe[dataframe["region"] == country]
    
    return dataframe

def save_data(dataframe: pd.DataFrame, save_path: str) -> None:
    """Saves the data inside a pandas dataframe."""
    dataframe.to_csv(save_path, index = False)

def __str_to_float(val: str) -> float:
    """Function to convert a string to float. If invalid returns NaN."""
    try:
        return float(re.search(r'\d+\.*\d*', val).group(0))
    except (ValueError, AttributeError):
        return np.nan
