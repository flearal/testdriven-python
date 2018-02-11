import unittest
from src.math import Math

class TestMathMethods(unittest.TestCase):

    def testFaculty4(self):
        x = 4
        result = 24
        self.assertEqual(Math().faculty(x), result)

    def testFaculty6(self):
        x = 6
        result = 720
        self.assertEqual(Math().faculty(x), result)


if __name__ == '__main__':
    unittest.main()
