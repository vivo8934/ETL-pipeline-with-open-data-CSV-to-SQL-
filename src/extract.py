import pandas as pd
from config import CSV_PATH
import os

def extract_weather_data(chunksize=100_000):
    if not os.path.exists(CSV_PATH):
        raise FileNotFoundError(f"CSV file not found at: {CSV_PATH}")
    
    try:
        print(f"Reading data from {CSV_PATH} in chunks of {chunksize}...")
        return pd.read_csv(CSV_PATH, chunksize=chunksize)
    except pd.errors.EmptyDataError:
        raise ValueError("CSV file is empty.")
    except pd.errors.ParserError as e:
        raise ValueError(f"Parsing error: {e}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error reading CSV: {e}")