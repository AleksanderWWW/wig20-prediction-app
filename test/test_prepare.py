import unittest

import pandas as pd

from app.models import prepare


class DataPreparationTest(unittest.TestCase):
    test_df = pd.DataFrame(
        {
            "col1": [i for i in range(10)],
            "col2": [2*i - 1 for i in range(10)]  
        }
    )

    def test_data_split(self):
        train, test = prepare.split_data(self.test_df, "col1")
        self.assertEqual(len(train), 7)
        self.assertEqual(len(test), 3)
