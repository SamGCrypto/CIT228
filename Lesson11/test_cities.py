import unittest

from city_function import make_city

class CountryTest(unittest.TestCase):
    """Tests for city_function.py."""
    def test_city_country_one(self):
        """Test for basics"""
        madeCity = make_city('Chili','South America')
        self.assertEqual(madeCity,"Chili, South America")
    def  test_city_country_population(self):
        """Test the population function"""
        madeCity = make_city('Chili','South America','100000')
        self.assertEqual(madeCity ,"Chili, South America, 100000")


if __name__ == '__main__':
    unittest.main()