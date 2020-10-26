import unittest
from city_functions import cities

class CityTestCase(unittest.TestCase):
    """test for city_functions.py"""
    def test_city_country(self):
        location = cities('accra','ghana')
        self.assertAlmostEqual(location,'Accra, Ghana')

if __name__ == '__main__' :
    unittest.main()