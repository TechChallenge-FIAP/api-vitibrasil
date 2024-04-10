from typing import List
from bs4 import BeautifulSoup
import requests
import pandas as pd

base_url = "http://vitibrasil.cnpuv.embrapa.br/download/"

res = requests.get(base_url)

if res.status_code == 200:
    soup = BeautifulSoup(res.content, "html.parser")

    files_href = soup.find_all("a", href=lambda href: href and ".csv" in href.lower())

    if files_href:
        files_list = [file["href"] for file in files_href if "csv" in file["href"]]
    else:
        print("Not Found")
else:
    print("Error")


for file in files_list:
    df = pd.read_csv(base_url + file, sep=None, engine="python")

    print(df.head())
