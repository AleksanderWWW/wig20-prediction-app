"""
Module used to scrape tickers from the stooq wig20 page.
This will provide the application with up-to-date list
of the index components.
"""

from typing import List, Dict

import requests

from bs4 import BeautifulSoup

from headers import headers


class ComponentScraper:
    URL_BASE = "https://stooq.pl/q/i/?s="

    def __init__(self, index: str ="wig20") -> None:
        self.index = index

    def set_index(self, new_index: str) -> None:
        self.index = new_index

    def _get_page_source(self, *request_args, **request_kwargs) -> str:
        # url = self.URL_BASE + self.index
        url = "https://stooq.pl/t/?i=532"
        response = requests.get(url, *request_args, *request_kwargs, headers=headers)

        if response.status_code != 200:
            raise Exception(f"GET request to url: {url} \
                return invalid response code ({response.status_code}")

        return response.text

    def _retrieve_tickers(self, soup: BeautifulSoup) -> List[str]:
        """Method iterates over table tags and scrapes the irst column values 
        (tickers) to a list."""
        tickers: List[str] = []

        table = soup.find("table", {"id": "fth1"}).find("tbody")

        rows: list = table.find_all("tr")
        for row in rows:
            # get content of the first cell
            ticker_cell = row.find("td")
            tickers.append(ticker_cell.text)

        return tickers

    def scrape_components(self, parser="lxml"):
        html_content = self._get_page_source()
        soup = BeautifulSoup(html_content, parser)
        return self._retrieve_tickers(soup)
    


if __name__ == "__main__":
    scraper = ComponentScraper()
    ticker_list = scraper.scrape_components()
    print(ticker_list)