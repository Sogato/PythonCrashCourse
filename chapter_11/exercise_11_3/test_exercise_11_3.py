import unittest
from chapter_11.exercise_11_3.exercise_11_3 import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        first_name = 'Иван'
        last_name = 'Иванович'
        salary = 50000
        self.test_employee = Employee(first_name, last_name, salary)

    def test_give_default_raise(self):
        self.test_employee.give_raise()

    def test_give_custom_raise(self):
        self.test_employee.give_raise(10000)


if __name__ == '__main__':
    unittest.main()
