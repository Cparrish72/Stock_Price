import unittest
from stock_data import fetch_stock_data
from pandas import DataFrame

class TestStockData(unittest.TestCase):

    def test_fetch_stock_data(self):

        data = fetch_stock_data("AAPL", "2021-01-01", "2021-01-10")
        self.assertIsInstance(data, DataFrame)
        self.assertFalse(data.empty)
        self.assertIn('Close', data.columns)

if __name__ == '__main__':
    unittest.main()
