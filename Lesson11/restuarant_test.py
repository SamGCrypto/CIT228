import unittest
from restuarant import Restaurant

class TestRestaurantFeatures(unittest.TestCase):
    def setUp(self):
        """Set up Test Case"""
        self.Restuarant = Restaurant("Asian", True, "Noodle Shop",200)
    def testServed(self):
        self.Restuarant.number_served_default(100)
        self.assertEqual(self.Restuarant.numServed,100)
    def testServedUpdate(self):
        self.Restuarant.number_served_updated(100)
        self.assertEqual(self.Restuarant.numServed,300)

if __name__ == '__main__':
    unittest.main()