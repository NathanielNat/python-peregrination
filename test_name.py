import unittest
from name_func import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Test case for name_function.py"""

    def test_first_last_name(self):
        """checking if names like Nathaniel Nat works"""
        formatted_name = get_formatted_name('abena','yao')
        self.assertEqual(formatted_name,'Abena Yao')

    def test_first_last_middle_name(self):
        """ checking if names like Nathaniel yaw Nat"""
        formatted_name = get_formatted_name('abena','yao','elorm')
        self.assertEqual(formatted_name,'Abena Elorm Yao')


if __name__ == '__main__' :
    unittest.main()