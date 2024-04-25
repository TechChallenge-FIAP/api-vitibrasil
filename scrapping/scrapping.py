import asyncio
import io
import time
from typing import List

from http import HTTPStatus
from venv import logger
from requests.exceptions import HTTPError
from urllib3.exceptions import NewConnectionError

import aiohttp
import pandas as pd
import requests
from bs4 import BeautifulSoup


retries: int = 3


async def get_csv_async(client: aiohttp.ClientSession, url: str, filename: str):

    for n in range(retries):
        try:
            async with client.get(url) as response:
                with io.StringIO(await response.text()) as text_io:
                    with open(f"tmp/{filename}", mode="w") as file:
                        print(text_io.getvalue(), file=file)
                response.raise_for_status()
        except Exception as e:
            logger.info("tentativa " + str(n))
            time.sleep(10)
            continue


async def get_all_csvs_async(urls):
    async with aiohttp.ClientSession() as client:
        futures = [
            get_csv_async(client, url, filename) for filename, url in urls.items()
        ]
        return await asyncio.gather(*futures)


base_url = "http://vitibrasil.cnpuv.embrapa.br/download/"

for n in range(retries):
    try:
        res = requests.get(base_url)
        res.raise_for_status()
    except Exception as e:
        logger.info("tentativa " + str(n))
        time.sleep(10)
        continue


if res.status_code == 200:
    soup = BeautifulSoup(res.content, "html.parser")

    files_href = soup.find_all("a", href=lambda href: href and ".csv" in href.lower())

    files_dict = {
        file["href"]: base_url + file["href"]
        for file in files_href
        if "csv" in file["href"]
    }

else:
    print("Error")


csv_files_list = asyncio.get_event_loop().run_until_complete(
    get_all_csvs_async(files_dict)
)
