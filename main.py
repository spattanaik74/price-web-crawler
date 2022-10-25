import csv
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup


def get_url(search_item):
    search_item = search_item.replace(' ', '+')
    link = f'https://www.flipkart.com/search?q={search_item}&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_8_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_8_0_na_na_na&as-pos=8&as-type=TRENDING&suggestionId=tv&requestId=9c9fa553-b7e5-454b-a65b-bbb7a9c74a29'
    return link


def extract_model(item):
    dict_data = {}

    page = requests.get(get_url(item))

    soup = BeautifulSoup(page.content, 'html.parser')

    for data in soup.findAll('div', class_='_2kHMtA'):
        dict_data[data.find('div', attrs={'class': '_4rR01T'}).text] = {
            'price': data.find('div', attrs={'class': '_30jeq3 _1_WHN1'}).text,
            'rating': data.find('div', attrs={'class': '_3LWZlK'}).text,
            'link': ['flipkart.com' + i['href'] for i in data][0]}

    return dict_data


# _3pLy-c row

model = extract_model('iphone')
for k, v in model.items():
    print(k, v)
