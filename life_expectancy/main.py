from pathlib import Path
from life_expectancy.data_loading import load_data, save_data
from life_expectancy.data_cleaning import clean_data

PROJECT_DIR = Path(__file__).parent
FILE_PATH = f"{PROJECT_DIR}/data/eu_life_expectancy_raw.tsv"
SAVE_PATH = "life_expectancy/data/pt_life_expectancy.csv"

def main(country: str = "PT") -> None: #pragma: no cover
    """Main function."""

    dataframe = load_data(FILE_PATH, '\t')

    cleaned_df = clean_data(dataframe, country)

    save_data(cleaned_df, SAVE_PATH)

    return cleaned_df
