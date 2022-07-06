import unittest
from datetime import date

import pandas as pd

from gpw import Wig20Scraper, parse_data



class ScraperTest(unittest.TestCase):
    start = date(2021, 7, 5)
    end = date(2022, 7, 5)
    
    def test_scraper_instantiates(self):
        try:
            scraper = Wig20Scraper(self.start, self.end)
            self.assertTrue(bool(scraper))
        except Exception as e:
            print(e)
            self.assertTrue(False)
            
    def test_build_url(self):
        correct_url = "https://gpwbenchmark.pl/chart-json.php?req=[{%22isin%22:%22PL9999999987%22,%22mode%22:%22RANGE%22,%22from%22:%222021-07-05%22,%22to%22:%222022-07-05%22}]"
        scraper = Wig20Scraper(self.start, self.end)
        url = scraper.build_url()
        self.assertEqual(correct_url, url)
        
    def test_get_data_returns_list(self):
        scraper = Wig20Scraper(self.start, self.end)
        data = scraper.get_data()
        
        self.assertTrue(type(data) is list)
        
    def test_get_data_correct_length(self):
        scraper = Wig20Scraper(self.start, self.end)
        data = scraper.get_data()
        
        self.assertEqual(len(data), 253)
        
        
class ParseFuncTest(unittest.TestCase):
    start = date(2021, 7, 5)
    end = date(2022, 7, 5)
    scraper = Wig20Scraper(start, end)
    data = scraper.get_data()
    
    def test_parse_data_returns_dataframe(self):
        data_parsed = parse_data(self.data)
        self.assertTrue(type(data_parsed) is pd.DataFrame)
        
    def test_parse_data_correct_length(self):
        data_parsed = parse_data(self.data)
        self.assertEqual(len(data_parsed), 253)        
        
            
if __name__ == "__main__":
    unittest.main()
