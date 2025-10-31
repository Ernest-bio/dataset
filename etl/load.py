import pandas as pd

def load_to_parquet(df: pd.DataFrame, output_path: str = "dinosaurs.parquet"):
    """Сохраняет датасет в формате Parquet."""
    print(f"[LOAD] Saving dataset to {output_path} ...")
    df.to_parquet(output_path, index=False)
    print("[LOAD] Done.")