import unittest
from datetime import date

from gpw import Wig20Scraper, parse_data



class ScraperTest(unittest.TestCase):
    start = date(2021, 7, 5)
    end = date(2022, 7, 5)
    
    def test_scraper_instantiates(self):
        try:
            scraper = Wig20Scraper(self.start, self.end)
            self.assertTrue(True)
        except Exception as e:
            print(e)
            self.assertTrue(False)
            
    def test_build_url(self):
        correct_url = "https://gpwbenchmark.pl/chart-json.php?req=[{%22isin%22:%22PL9999999987%22,%22mode%22:%22RANGE%22,%22from%22:%222021-07-05%22,%22to%22:%222022-07-05%22}]"
        scraper = Wig20Scraper(self.start, self.end)
        url = scraper.build_url()
        self.assertEqual(correct_url, url)
        
            
if __name__ == "__main__":
    unittest.main()
