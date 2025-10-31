import pandas as pd

FILE_ID = "1C3pyOhWaMakoxML6MRnJDwYR5Z2xWAj-"  

def extract_from_gdrive() -> pd.DataFrame:
    """Извлекает исходные данные о динозаврах с Google Drive."""
    file_url = f"https://drive.google.com/uc?id={FILE_ID}"
    print(f"[EXTRACT] Loading dataset from {file_url}")
    df = pd.read_csv(file_url)
    print(f"[EXTRACT] Extracted {len(df)} rows.")
    return df