"""
Loading/saving script
"""

from pathlib import Path
from typing import Union
import pandas as pd

def load_data(file_path: Union[Path, str], sep: str = ",") -> pd.DataFrame:
    """Loads a CSV file given a path and separator."""
    return pd.read_csv(file_path, sep=sep)

def save_data(dataframe: pd.DataFrame, save_path: str) -> None:
    """Saves the data inside a pandas dataframe."""
    dataframe.to_csv(save_path, index = False)
