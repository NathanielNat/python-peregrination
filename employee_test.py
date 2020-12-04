import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Eployee class test"""
    def setup(self):
        self.first_name = 'Nathaniel'
        self.last_name = 'Agbenyenu'
        self.salary = 8000
        self.new_employee  = Employee()

    def test_give_default_raise(self):
        """Test foro default value"""
        new_salary = self.new_employee.give_raise()
        self.assertEqual(new_salary,13000)

    def test_give_custom_raise(self):
        """ Test for accepted value"""
        custom_raise = 10000
        new_salary = self.give_raise(new_raise)
        self.assertEqaul(new_salary,18000)

if __name__ == '__main__':
    unittest.main()
