import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine


load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_URL = os.getenv("DB_URL")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

TABLE_NAME = "bolotov"  


DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_URL}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL, pool_recycle=3600)


parquet_path = "dinosaurs.parquet"
df = pd.read_parquet(parquet_path)


df.rename(columns={col: col.lower() for col in df.columns}, inplace=True)


df_sample = df.head(100)


df_sample.to_sql(
    name=TABLE_NAME,
    con=engine,
    schema="public",
    if_exists="replace",  
    index=False
)


with engine.connect() as conn:
    result = pd.read_sql(f"SELECT * FROM public.{TABLE_NAME} LIMIT 6", conn)
    print(result)

print(f"Данные успешно записаны в таблицу '{TABLE_NAME}' базы '{DB_NAME}'")