"""
Cleaning script
"""

import re
import pandas as pd
import numpy as np

def main(): #pragma: no cover
    """Main function."""

    file_path = "life_expectancy/data/eu_life_expectancy_raw.tsv"
    dataframe = load_data(file_path, '\t')

    col_to_split = 'unit,sex,age,geo\\time'
    splitted_cols_list = ['unit', 'sex', 'age', 'region']
    cleaned_df = clean_data(dataframe, col_to_split, splitted_cols_list, "PT")

    save_path = "life_expectancy/data/pt_life_expectancy.csv"
    save_data(cleaned_df, save_path)


def load_data(file_path, sep = ","):
    """Loads a CSV file given a path and separator."""
    return pd.read_csv(file_path, sep=sep)
    

def clean_data(dataframe, col_to_split, splitted_cols_list, country):
    """Function that will clean, transform and filter (by region, its default being PT) the life_expectancy data."""
    
    # Split first column
    dataframe[splitted_cols_list] = dataframe[col_to_split].str.split(",", expand=True)
    dataframe = dataframe.drop(columns=col_to_split)

    # Unpivot data
    dataframe = pd.melt(dataframe, id_vars=splitted_cols_list, var_name="year", value_name="value")
    
    # Apply some conversions
    dataframe["year"] = pd.to_numeric(dataframe["year"], errors="coerce").astype(int)

    # Apply the str_to_float method and perform data cleaning
    dataframe['value'] = [str_to_float(val) for val in dataframe['value']]

    # Remove natural NaNs, but also the coerced invalid values from the previous value conversion
    dataframe.dropna(subset=["value"], inplace=True)

    # Filter by region
    dataframe = dataframe[dataframe["region"] == country]
    
    return dataframe

def save_data(dataframe, save_path):
    """Saves the data inside a pandas dataframe."""
    dataframe.to_csv(save_path, index = False)

def str_to_float(val):
    """Function to convert a string to float. If invalid returns NaN."""
    try:
        return float(re.search(r'\d+\.*\d*', val).group(0))
    except (ValueError, AttributeError):
        return np.nan
