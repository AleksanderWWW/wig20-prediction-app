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
            
            
if __name__ == "__main__":
    unittest.main()
