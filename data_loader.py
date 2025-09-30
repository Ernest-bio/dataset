import pandas as pd

FILE_ID = "1C3pyOhWaMakoxML6MRnJDwYR5Z2xWAj-"  
file_url = f"https://drive.google.com/uc?id={FILE_ID}"

raw_data = pd.read_csv(file_url)

raw_data['length_m'] = pd.to_numeric(raw_data['length_m'], errors='coerce')
raw_data['weight_kg'] = pd.to_numeric(raw_data['weight_kg'], errors='coerce')
raw_data['height_m'] = pd.to_numeric(raw_data['height_m'], errors='coerce')


raw_data['first_discovered'] = pd.to_datetime(raw_data['first_discovered'], errors='coerce')


raw_data = raw_data.astype({
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


print(raw_data.head(10))
print(raw_data.dtypes)

raw_data.to_parquet("dinosaurs.parquet", index=False)
