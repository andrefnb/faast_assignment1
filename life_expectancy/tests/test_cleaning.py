"""Tests for the cleaning module"""
import pandas as pd

from life_expectancy.cleaning import load_data, clean_data, save_data
from . import OUTPUT_DIR


def test_clean_data(pt_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""

    file_path = "life_expectancy/data/eu_life_expectancy_raw.tsv"
    dataframe = load_data(file_path, '\t')

    col_to_split = 'unit,sex,age,geo\\time'
    splitted_cols_list = ['unit', 'sex', 'age', 'region']
    cleaned_df = clean_data(dataframe, col_to_split, splitted_cols_list, "PT")

    save_path = "life_expectancy/data/pt_life_expectancy.csv"
    save_data(cleaned_df, save_path)

    pt_life_expectancy_actual = pd.read_csv(
        OUTPUT_DIR / "pt_life_expectancy.csv"
    )
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )
