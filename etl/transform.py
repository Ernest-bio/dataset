import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Преобразует типы данных и очищает таблицу динозавров."""
    print("[TRANSFORM] Cleaning and transforming data...")

    # Приведение типов
    for col in ['length_m', 'weight_kg', 'height_m']:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df['first_discovered'] = pd.to_datetime(df['first_discovered'], errors='coerce')

    df = df.astype({
        'scientific_name': str,
        'common_name': str,
        'meaning': str,
        'diet': str,
        'locomotion': str,
        'geological_period': str,
        'lived_in': str,
        'behavior_notes': str,
        'fossil_location': str,
        'notable_features': str,
        'intelligence_level': str,
        'source_link': str,
        'row_index': int
    })

    print("[TRANSFORM] Transformation complete.")
    return df