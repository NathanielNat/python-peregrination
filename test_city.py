from cities_new import format_cities

import unittest

class FormatNametest(unittest.TestCase):
    """Test for a well formatted city name"""
    def test_city_country(self):
        """ do city names  like Accra, Ghana work?"""
        formatted_name = format_cities('accra','ghana')
        self.assertEqual(formatted_name,'Accra, Ghana')

    def test_city_country_population(self):
        formatted_name = format_cities('accra','ghana',9000)
        self.assertEqual(formatted_name,'Accra, Ghana - Population 9000')


if __name__  == '__main__':
    unittest.main()