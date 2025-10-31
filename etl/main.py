from extract import extract_from_gdrive
from transform import transform_data
from load import load_to_parquet

def main():
    print("[MAIN] Starting DDE ETL pipeline...")
    df = extract_from_gdrive()
    df_transformed = transform_data(df)
    load_to_parquet(df_transformed)
    print("[MAIN] ETL pipeline complete.")

if __name__ == "__main__":
    main()
