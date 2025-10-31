import requests
import pandas as pd

url = "https://rickandmortyapi.com/api/character"

response = requests.get(url)
data = response.json() 

characters = data["results"]

df = pd.DataFrame(characters)

print(df.head(10))

df.to_csv("rick_and_morty_characters.csv", index=False)
