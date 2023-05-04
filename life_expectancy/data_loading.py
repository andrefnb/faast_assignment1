"""
Loading/saving script
"""

from pathlib import Path
from typing import Union
import pandas as pd

from life_expectancy.loading_strategy import LoadingStrategy

def load_data(strategy: LoadingStrategy, file_path: Union[Path, str], sep: str = ",") -> pd.DataFrame:
    """Loads data given a path."""
    return strategy.load_data(file_path, sep)

def save_data(dataframe: pd.DataFrame, save_path: str) -> None:
    """Saves the data inside a pandas dataframe."""
    dataframe.to_csv(save_path, index = False)
