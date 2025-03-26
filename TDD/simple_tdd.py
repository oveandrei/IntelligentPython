import unittest

class TestPrimeNumber(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(4))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True



if __name__ == '__main__':
 unittest.main()