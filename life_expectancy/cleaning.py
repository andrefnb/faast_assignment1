"""
Cleaning script
"""

import re
import argparse
import pandas as pd
import numpy as np

def clean_data(country):
    """Function that will clean, transform and filter (by region, its default being PT) the life_expectancy data."""
    
    # Load data
    dataframe = pd.read_csv("life_expectancy/data/eu_life_expectancy_raw.tsv", sep='\t')

    # Initialize some vars
    col_to_split = 'unit,sex,age,geo\\time'
    splitted_cols_list = ['unit', 'sex', 'age', 'region']
    
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

    # Save transformed data
    dataframe.to_csv("life_expectancy/data/pt_life_expectancy.csv", index = False)

def str_to_float(val):
    """Function to convert a string to float. If invalid returns NaN."""
    try:
        return float(re.search(r'\d+\.*\d*', val).group(0))
    except (ValueError, AttributeError):
        return np.nan

if __name__ == "__main__":  # pragma: no cover

     # Create argument parser for debugging
    parser = argparse.ArgumentParser(description='Transformed life expectancy data filtered by country')
    parser.add_argument('--country', type=str, default='PT', help='Country code to filter')
    args = parser.parse_args()
    clean_data(args.country)
