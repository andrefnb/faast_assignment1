"""
Cleaning script
"""

import re
import pandas as pd
import numpy as np

COL_TO_SPLIT = 'unit,sex,age,geo\\time'
SPLITTED_COLS_LIST = ['unit', 'sex', 'age', 'region']
    
def clean_data(dataframe: pd.DataFrame, country: str) -> pd.DataFrame:
    """Function that will clean, transform and filter (by region, its default being PT) the life_expectancy data."""

    # Make a copy
    dataframe = dataframe.copy()
    
    # Split first column
    dataframe[SPLITTED_COLS_LIST] = dataframe[COL_TO_SPLIT].str.split(",", expand=True)
    dataframe = dataframe.drop(columns=COL_TO_SPLIT)

    # Unpivot data
    dataframe = pd.melt(dataframe, id_vars=SPLITTED_COLS_LIST, var_name="year", value_name="value")
    
    # Apply some conversions
    dataframe["year"] = pd.to_numeric(dataframe["year"], errors="coerce").astype(int)

    # Apply the str_to_float method and perform data cleaning
    dataframe['value'] = [__str_to_float(val) for val in dataframe["value"]]

    # Remove natural NaNs, but also the coerced invalid values from the previous value conversion
    dataframe.dropna(subset=["value"], inplace=True)

    # Filter by region
    dataframe = dataframe[dataframe["region"] == country]
    
    return dataframe.reset_index(drop = True)

def __str_to_float(val: str) -> float:
    """Function to convert a string to float. If invalid returns NaN."""
    try:
        return float(re.search(r'\d+\.*\d*', val).group(0))
    except (ValueError, AttributeError):
        return np.nan
