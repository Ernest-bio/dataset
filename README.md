## Описание
Этот репозиторий содержит скрипты для:

1. Загрузки CSV-датасета динозавров с Google Drive.
2. Преобразования типов колонок и сохранения в Parquet.

---

## 1. Требования

- Python 3.10+  
- Conda (рекомендуется) 
- Установленные библиотеки:
`pip install pandas pyarrow`

---

## 2. Рекомендуется создать окружение conda
Создание и активация conda окружения:
`conda create -n dinosaurs_env python=3.10
conda activate dinosaurs_env`

---

## 3. Загрузка Dataset

Файл: data_loader.py

Запусти скрипт:

`python download_to_parquet.py`

CSV скачивается с Google Drive.

Столбцы приводятся к нужным типам (numeric, datetime, str, int).

Результат сохраняется в dinosaurs.parquet

---

Проверить запись данных можно скриптом:
```python
import pandas as pd

df = pd.read_parquet("dinosaurs.parquet")
print(df.head(10))
print(df.dtypes)
```
---

## 4. Ссылка на dataset, загруженный на Google drive: 
https://drive.google.com/file/d/1C3pyOhWaMakoxML6MRnJDwYR5Z2xWAj-/view?usp=sharing

---

## 5. Исходник данных с сайта kaggle: 
https://www.kaggle.com/datasets/canozensoy/dinosaur-genera-dataset?resource=download

---
## 6. Результаты работы:

## Первые 10 строк после выполнения команды raw_data.head(10)
<img width="1571" height="1010" alt="image" src="https://github.com/user-attachments/assets/068a60cb-0753-4485-9c35-22a5dd270b08" />

## Приведение типов
<img width="1782" height="439" alt="image" src="https://github.com/user-attachments/assets/b58c3b81-8313-4fb9-86d0-fcd0782ae1bb" />

---

## 7. Рендер ноутбука с EDA
[Рендер ноутбука с EDA через nbviewer](https://nbviewer.org/github/Ernest-bio/dataset/blob/main/notebooks/EDA.ipynb)
