import unittest
from unittest.mock import patch
import main
import datetime


class TestMain(unittest.TestCase):

    @patch('main.input', return_value="GOOGL")
    def test_get_stock_symbol(self, input):
        self.assertEqual((main.get_stock_symbol()).isalpha(), True)
        self.assertEqual((main.get_stock_symbol()).isupper(), True)

        if 7 >= len(main.get_stock_symbol()) > 0:
            self.assertTrue("1-7 characters")
        else:

            self.assertFalse('Too Long')

    @patch('main.input', return_value="1")
    def test_get_chart_type(self, input):
        if int(main.get_stock_symbol()) in range(1,4):
            self.assertTrue("1 or 2")
        else:
            self.assertFalse('not 1 or 2')
        self.assertEqual(len(main.get_chart_type()), 1)
        self.assertEqual((main.get_chart_type()).isnumeric(), True)

    @patch('main.input', return_value="1")
    def test_get_time_series(self, input):
        pass
        if main.get_stock_symbol() == "1" or main.get_stock_symbol() == "2":
            self.assertTrue("1-4")
        else:
            self.assertFalse('not 1-4')
        self.assertEqual(len(main.get_chart_type()), 1)
        self.assertEqual((main.get_chart_type()).isnumeric(), True)

    @patch('main.input', return_value="1999-1-1")
    def test_get_beginning_date(self, input):
        self.assertEqual(str(main.get_beginning_date()), "1999-01-01")

    @patch('main.input', return_value="1999-1-1")
    def test_get_end_date(self, input):
        self.assertEqual(str(main.get_end_date(datetime.date(1990, 1, 1))), "1999-01-01")


if __name__ == '__main__':
    unittest.main()