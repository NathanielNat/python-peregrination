import unittest
from city_functions import cities

class CityTestCase(unittest.TestCase):
    """test for city_functions.py"""
    def test_city_country(self):
        location = cities('accra','ghana')
        self.assertEqual(location,'Accra, Ghana')

    def test_city_country_population(self):
        location = cities('accra','ghana','30000000')
        self.assertEqual(location,'Accra, Ghana - Population 30000000')

if __name__ == '__main__' :
    unittest.main()