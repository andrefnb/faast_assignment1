"""Tests for the region enum"""
import numpy as np

from life_expectancy.region import list_all_countries

def test_regions_list(all_regions_expected):
    """Test for the region listing function"""

    region_list = list_all_countries()
    np.testing.assert_array_equal(
        region_list, all_regions_expected
    )
