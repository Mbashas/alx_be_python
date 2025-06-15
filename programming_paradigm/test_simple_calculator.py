import unittest
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_add(self):
        #addition = SimpleCalculator.add(2,3)
        self.assertEqual(self.calc.add(3,2), 5 )
    def test_sub(self):
        #difference = SimpleCalculator.subtract(3,2)
        self.assertEqual(self.calc.subtract(3,2), 1)
    def test_product(self):
        #product =SimpleCalculator.multiply(2,3)
        self.assertEqual(self.calc.multiply(3,2),6)
    def test_division(self):
        #division = SimpleCalculator.divide(4,4)
        self.assertEqual(self.calc.divide(4,4),1)
    def test_zeroError(self):
        #zeroErr=SimpleCalculator.divide(2,0)
        self.assertIsNone(self.calc.divide(2, 0))


"""
There are a few issues with your test implementation:
In test_zeroError, you're comparing the result to ZeroDivisionError class itself, not an instance. The divide method returns None for zero division, so the test should be:
self.assertIsNone(self.calc.divide(2, 0))
The commented-out code in each test method is incorrect - you're trying to call methods as static methods (using the class name) when they are instance methods.
Your test names could be more descriptive (e.g., test_sub should be test_subtract).
You're not testing edge cases or negative numbers.
The main issue is the zero division test, as it's currently written incorrectly and will fail. The other points are more about best practices than actual errors.
"""