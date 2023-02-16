import unittest
from chapter_11.exercise_11_1.exercise_11_1 import set_address


class NamesTestCase(unittest.TestCase):
    def test_set_address(self):
        address = set_address('Россия', 'Калининград')
        self.assertEqual(address, 'Россия, Калининград')


if __name__ == '__main__':
    unittest.main()
