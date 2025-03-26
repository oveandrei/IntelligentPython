
def add(a, b):
 return a + b


import unittest
class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(1, 0), 1)
        self.assertEqual(add(0, 1), 1)
        self.assertEqual(add(-1, 0), -1)



if __name__ == '__main__':
    unittest.main()
