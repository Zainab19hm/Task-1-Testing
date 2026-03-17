import unittest
from main import add_numbers, divide_numbers

class TestMain(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 6)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertAlmostEqual(add_numbers(0.1, 0.2), 0.3)
        self.assertAlmostEqual(add_numbers(-1, -2), -3)

    def test_divide_numbers(self):
        self.assertEqual(divide_numbers(10, 2), 5)
        # Test division by zero exception
        with self.assertRaises(ValueError):
            divide_numbers(10, 0)

if __name__ == "__main__":
    unittest.main()
