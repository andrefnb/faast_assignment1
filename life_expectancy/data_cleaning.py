"""
Cleaning script
"""

import pandas as pd

from life_expectancy.region import Region
from life_expectancy.cleaning_strategy import CleaningStrategy

COL_TO_SPLIT = 'unit,sex,age,geo\\time'
SPLITTED_COLS_LIST = ['unit', 'sex', 'age', 'region']
    
def clean_data(strategy: CleaningStrategy, dataframe: pd.DataFrame, country: Region) -> pd.DataFrame:
    """Function that will clean, transform and filter (by region, its default being PT) the life_expectancy data using a certain strategy for each format."""
    return strategy.clean_data(dataframe, country)
    