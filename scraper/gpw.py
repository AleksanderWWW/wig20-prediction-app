from datetime import date
from typing import List, Dict

import requests
import pandas as pd


class Wig20Scraper:

    def __init__(self, from_date: date, to_date: date) -> None:
        self.from_date = from_date
        self.to_date = to_date

    def build_url(self) -> str:
        base: str = "https://gpwbenchmark.pl/chart-json.php"
        from_date_str = self.from_date.strftime("%Y-%m-%d")
        to_date_str = self.to_date.strftime("%Y-%m-%d")
        req: str = "[{%22isin%22:%22PL9999999987%22,%22mode%22:%22RANGE%22,%22from%22:%22" + \
                    from_date_str + \
                    "%22,%22to%22:%22" + \
                    to_date_str + \
                    "%22}]"

        return base + "?req=" + req

    def get_data(self) -> list:
        url = self.build_url()
        response = requests.get(url)
        return response.json()[0]["data"]


def parse_data(data: List[Dict[str, float]]) -> pd.DataFrame:
    data_dict = {
        "date": [],
        "open": [],
        "close": [],
        "min": [],
        "max": []
    }

    for item in data:
        data_dict["date"].append(date.fromtimestamp(item["t"]))
        data_dict["open"].append(item["o"])
        data_dict["close"].append(item["c"])
        data_dict["min"].append(item["l"])
        data_dict["max"].append(item["h"])

    return pd.DataFrame(data_dict)


if __name__ == "__main__":
    start = date(2021, 7, 5)
    end = date(2022, 7, 5)
    scraper = Wig20Scraper(start, end)
    data = scraper.get_data()
    wig20_df = parse_data(data)
    print(wig20_df)