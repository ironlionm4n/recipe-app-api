"""
Sample test cases for the app
"""

from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):
    """
    Test Calc class
    """
    def test_add(self):
        """
        Test add function
        """
        self.assertEqual(calc.add(3, 8), 11)
        self.assertEqual(calc.add(-3, 8), 5)
        self.assertEqual(calc.add(-3, -8), -11)
        self.assertEqual(calc.add(3, -8), -5)

    def test_subtract_numbers(self):
        """
        Test subtract numbers
        """
        self.assertEqual(calc.subtract(3, 8), -5)
