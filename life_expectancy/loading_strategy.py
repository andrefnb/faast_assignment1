"""
Python file containing the loading strategy pattern.
"""

from pathlib import Path
from typing import Union
import zipfile
from abc import ABC, abstractmethod
import pandas as pd

PROJECT_DIR = Path(__file__).parent
DATA_PATH = PROJECT_DIR / "data"
DECOMPRESSED_PATH = DATA_PATH / "decompressed"
DECOMPRESSED_FILE_PATH = DECOMPRESSED_PATH / "eurostat_life_expect.json"

class LoadingStrategy(ABC):
    """Loading strategy abstract class"""

    @abstractmethod
    def load_data(self, file_path: Union[Path, str], sep: str = ",") -> pd.DataFrame:
        """Definition of the data loading function target of the strategy pattern"""

class ConcreteLoadingStrategyCSV(LoadingStrategy):
    """
    Concrete strategy class for data loading in the CSV format
    """
    def load_data(self, file_path: Union[Path, str], sep: str = ",") -> pd.DataFrame:
        """Loads a CSV file given a path and separator."""
        return pd.read_csv(file_path, sep=sep)
    
class ConcreteLoadingStrategyCompactedJSON(LoadingStrategy):
    """
    Concrete strategy class for data loading in the CSV format
    """
    def load_data(self, file_path: Union[Path, str], sep: str = None) -> pd.DataFrame:
        """Loads a CSV file given a path and separator."""

        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall(DECOMPRESSED_PATH)
            return pd.read_json(DECOMPRESSED_FILE_PATH)
    