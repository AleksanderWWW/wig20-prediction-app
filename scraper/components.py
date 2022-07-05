"""
Module used to scrape tickers from the stooq wig20 page.
This will provide the application with up-to-date list
of the index components.
"""
import requests
import pandas as pd

from bs4 import BeautifulSoup


class ComponentScraper:
    URL_BASE = "https://stooq.pl/q/i/?s="

    def __init__(self, index: str ="wig20") -> None:
        self.index = index

    def set_index(self, new_index: str) -> None:
        self.index = new_index

    def _get_page_source(self, *request_args, **request_kwargs) -> str:
        url = self.URL_BASE + self.index
        response = requests.get(url, *request_args, *request_kwargs)

        if response.status_code != 200:
            raise Exception(f"GET request to url: {url} \
                return invalid response code ({response.status_code}")

        return response.text
