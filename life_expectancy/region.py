"""Region enum script"""
from enum import Enum

# class syntax
class Region(Enum):
    """Region enum for country selection."""
    EN = "EN"
    PT = "PT"

def list_all_countries() -> str:
    """Lists all values for the region enum"""
    return [region.value for region in Region]
        