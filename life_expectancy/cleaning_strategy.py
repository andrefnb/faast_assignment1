"""
Python file containing the loading strategy pattern.
"""

from abc import ABC, abstractmethod
import re
import pandas as pd
import numpy as np
from life_expectancy.region import Region

COL_TO_SPLIT = 'unit,sex,age,geo\\time'
SPLITTED_COLS_LIST = ['unit', 'sex', 'age', 'region']

class CleaningStrategy(ABC):
    """Cleaning strategy abstract class"""

    @abstractmethod
    def clean_data(self, dataframe: pd.DataFrame, country: Region) -> pd.DataFrame:
        """Definition of the data cleaning function target of the strategy pattern"""


class ConcreteCleaningStrategyCSV(CleaningStrategy):
    """
    Concrete strategy class for data loading in the CSV format
    """
    def clean_data(self, dataframe: pd.DataFrame, country: Region) -> pd.DataFrame:
        """Cleans a CSV file given a dataframe and the country enum to filter."""
        
        # Make a copy
        dataframe = dataframe.copy()
        
        # Split first column
        dataframe[SPLITTED_COLS_LIST] = dataframe[COL_TO_SPLIT].str.split(",", expand=True)
        dataframe = dataframe.drop(columns=COL_TO_SPLIT)

        # Unpivot data
        dataframe = pd.melt(dataframe, id_vars=SPLITTED_COLS_LIST, var_name="year", value_name="value")
        
        # Apply some conversions
        dataframe["year"] = pd.to_numeric(dataframe["year"], errors="coerce").astype("int64")

        # Apply the str_to_float method and perform data cleaning
        dataframe['value'] = [str_to_float(val) for val in dataframe["value"]]

        # Remove natural NaNs, but also the coerced invalid values from the previous value conversion
        dataframe.dropna(subset=["value"], inplace=True)

        # Filter by region
        dataframe = dataframe[dataframe["region"] == country.value]
        
        return dataframe.reset_index(drop = True)
    
class ConcreteCleaningStrategyCompactedJSON(CleaningStrategy):
    """
    Concrete strategy class for data loading in the JSON format
    """
    def clean_data(self, dataframe: pd.DataFrame, country: Region) -> pd.DataFrame:
        """Cleans a JSON file given a dataframe and the country enum to filter."""

        dataframe = pd.DataFrame(dataframe)

        # Make a copy
        dataframe = dataframe.copy()

        # Select relevant columns
        dataframe = dataframe[["unit", "sex", "age", "country", "year", "life_expectancy"]]

        # Rename to unified data structure
        dataframe = dataframe.rename(
            columns={"country": "region", "life_expectancy": "value"}
        )
        
        # Filter by region
        dataframe = dataframe[dataframe["region"] == country.value]

        return dataframe.reset_index(drop = True)
    
def str_to_float(val: str) -> float:
    """Function to convert a string to float. If invalid returns NaN."""
    try:
        return float(re.search(r'\d+\.*\d*', val).group(0))
    except (ValueError, AttributeError):
        return np.nan
    