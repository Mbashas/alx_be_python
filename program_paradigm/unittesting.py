'''import unittest

def add(x, y):
  """Returns the sum of two numbers."""
  return x + y

class TestAdd(unittest.TestCase):

  def test_add_positive(self):
    result = add(5, 3)
    self.assertEqual(result, 8)

  def test_add_negative(self):
    result = add(-2, 7)
    self.assertEqual(result, 5)

if __name__ == "__main__":
  unittest.main()'''

import unittest


def adding_number(number1, number2):
    return number1/number2

class TestPower(unittest.TestCase):
    def test_add(self):
        result=adding_number(8,9)
        self.assertEqual(result, 17)
    def test_minus(self):
        result=adding_number(90,43)
        self.assertEqual(result,58)
# Text Test Runner
if __name__ == "__main__":
    unittest.main()