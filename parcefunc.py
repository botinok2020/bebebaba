import requests      # Библиотека для отправки запросов
import re
import numpy as np   # Библиотека для матриц, векторов и линала
import pandas as pd  # Библиотека для табличек
import time          # Библиотека для тайм-менеджмента
from bs4 import BeautifulSoup

url = 'https://www.avito.ru/novosibirsk/kvartiry/sdam/na_dlitelnyy_srok'

response = requests.get(url)
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

def datall() -> str:

    nameu = []
    name = []

    nameu = soup.findAll('a', class_ = 'styles-module-root-m3BML styles-module-root_noVisited-HHF0s')
    for data in nameu:
        if data.find('h3', itemprop = 'name') is not None:
            name.append(data.text)
    return '\n'.join(name)
