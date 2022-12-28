import unittest
from prime import is_prime

class Tests(unittest.TestCase):

    def test_1(self):
        """check that 1 is not prime"""
        self.assertFalse(is_prime(1))

    def test_2(self):
        """check that 2 is prime"""
        self.assertTrue(is_prime(2))

    def test_3(self):
        """check that 9 is not prime"""
        self.assertFalse(is_prime(9))

    def test_4(self):
        """check that 11 is prime"""
        self.assertTrue(is_prime(11))

    def test_5(self):
        """check that 19 is prime"""
        self.assertTrue(is_prime(19))

    def test_6(self):
        """check that 20 is not prime"""
        self.assertFalse(is_prime(20))

if __name__ == "__main__":
    unittest.main()