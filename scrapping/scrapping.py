from typing import List
from bs4 import BeautifulSoup
import requests
import pandas as pd

import io
import asyncio

import aiohttp


async def get_csv_async(client, url):
    async with client.get(url) as response:
        with io.StringIO(await response.text()) as text_io:
            return pd.read_csv(text_io, sep=None, engine="python")


async def get_all_csvs_async(urls):
    async with aiohttp.ClientSession() as client:
        futures = [get_csv_async(client, url) for url in urls]
        return await asyncio.gather(*futures)


base_url = "http://vitibrasil.cnpuv.embrapa.br/download/"

res = requests.get(base_url)

if res.status_code == 200:
    soup = BeautifulSoup(res.content, "html.parser")

    files_href = soup.find_all("a", href=lambda href: href and ".csv" in href.lower())

    files_url = [
        base_url + file["href"] for file in files_href if "csv" in file["href"]
    ]
else:
    print("Error")


csv_files_list = asyncio.get_event_loop().run_until_complete(
    get_all_csvs_async(files_url)
)


for csv in csv_files_list:
    print(csv)
