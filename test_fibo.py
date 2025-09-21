import unittest
from fibo import fibo

class TestFibo(unittest.TestCase):
    def test_first_fibonacci(self):
        self.assertEqual(fibo(1), 0)

    def test_second_fibonacci(self):
        self.assertEqual(fibo(2), 1)

    def test_third_fibonacci(self):
        self.assertEqual(fibo(3), 1)

    def test_tenth_fibonacci(self):
        self.assertEqual(fibo(10), 34)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            fibo(0)
        with self.assertRaises(ValueError):
            fibo(-5)

if __name__ == "__main__":
    unittest.main()
