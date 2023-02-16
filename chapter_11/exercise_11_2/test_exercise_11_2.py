import unittest
from chapter_11.exercise_11_2.exercise_11_2 import set_address


class NamesTestCase(unittest.TestCase):
    def test_set_address(self):
        address = set_address('Россия', 'Калининград')
        self.assertEqual(address, 'Россия, Калининград')

    def test_population(self):
        address = set_address('Россия', 'Калининград', 500000)
        self.assertEqual(address, 'Россия, Калининград - Население 500000')


if __name__ == '__main__':
    unittest.main()
