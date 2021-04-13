import unittest
from employee import Employee

class TestEmployeeClass(unittest.TestCase):
    def setUp(self):
        """Create a test case"""
        self.myEmployee = Employee("Larry","Cable",5000)
    def test_increase_salary(self):
        self.myEmployee.give_raise()
        self.assertEqual(10000, self.myEmployee.salary)
    def test_custom_salary(self):
        self.myEmployee.give_raise(10000)
        self.assertEqual(15000, self.myEmployee.salary)


if __name__ == '__main__':
    unittest.main()
    