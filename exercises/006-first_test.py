import math
import unittest

# formula: Q = sqrt((2*C*D)/H) , where C=50 and H=30

def q_formula(D: int) -> int:
    C = 50
    H = 30

    return round(math.sqrt((2*C*D)/H))


class TestQ(unittest.TestCase):
    def test_100(self):
        input = 100
        expected = 18
        self.assertEqual(expected, q_formula(input))

    def test_150(self):
        input = 150
        expected = 22
        self.assertEqual(expected, q_formula(input))

    def test_180(self):
        input = 180
        expected = 24
        self.assertEqual(expected, q_formula(input))

if __name__ == '__main__':
    unittest.main()