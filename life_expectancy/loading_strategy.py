"""
Python file containing the loading strategy pattern.
"""

from pathlib import Path
from typing import Union
from typing import List
import zipfile
from abc import ABC, abstractmethod
import pandas as pd

PROJECT_DIR = Path(__file__).parent
DATA_PATH = PROJECT_DIR / "data"
DECOMPRESSED_PATH = DATA_PATH / "decompressed"
DECOMPRESSED_FILE_PATH = DECOMPRESSED_PATH / "eurostat_life_expect.json"

class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def load_data(self, file_path: Union[Path, str], sep: str = ","):
        """Definition of the data loading function target of the strategy pattern"""


class ConcreteStrategyCSV(Strategy):
    """
    Concrete strategy class for data loading in the CSV format
    """
    def load_data(self, file_path: Union[Path, str], sep: str = ",") -> List:
        """Loads a CSV file given a path and separator."""
        return pd.read_csv(file_path, sep=sep)
    
class ConcreteStrategyCompactedJSON(Strategy):
    """
    Concrete strategy class for data loading in the CSV format
    """
    def load_data(self, file_path: Union[Path, str], sep: str = None) -> List:
        """Loads a CSV file given a path and separator."""
        # data_decompressed = zlib.decompress()
        # return pd.read_json(file_path)

        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall(DECOMPRESSED_PATH)
            return pd.read_json(DECOMPRESSED_FILE_PATH)
    