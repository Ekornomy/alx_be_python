import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        """Test the addition method with various scenarios."""
        # Test basic addition
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 5), 15)
        
        # Test addition with zero
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(7, 0), 7)
        self.assertEqual(self.calc.add(0, 0), 0)
        
        # Test addition with negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(10, -3), 7)
        
        # Test addition with decimal numbers
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertEqual(self.calc.add(0.1, 0.2), 0.3)
    
    def test_subtraction(self):
        """Test the subtraction method with various scenarios."""
        # Test basic subtraction
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 5), 5)
        
        # Test subtraction with zero
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        
        # Test subtraction with negative numbers
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(10, -3), 13)
        
        # Test subtraction with decimal numbers
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)
        self.assertEqual(self.calc.subtract(0.3, 0.1), 0.2)
    
    def test_multiplication(self):
        """Test the multiplication method with various scenarios."""
        # Test basic multiplication
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(10, 5), 50)
        
        # Test multiplication with zero
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        
        # Test multiplication with one
        self.assertEqual(self.calc.multiply(5, 1), 5)
        self.assertEqual(self.calc.multiply(1, 5), 5)
        
        # Test multiplication with negative numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(2, -3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        
        # Test multiplication with decimal numbers
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertEqual(self.calc.multiply(0.5, 0.5), 0.25)
    
    def test_division(self):
        """Test the division method with various scenarios."""
        # Test basic division
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        
        # Test division with zero as numerator
        self.assertEqual(self.calc.divide(0, 5), 0)
        
        # Test division with negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)
        
        # Test division with decimal numbers
        self.assertEqual(self.calc.divide(5.5, 2), 2.75)
        self.assertEqual(self.calc.divide(1, 2), 0.5)
        
        # Test division that results in decimal
        self.assertEqual(self.calc.divide(1, 3), 1/3)
    
    def test_division_by_zero(self):
        """Test division by zero returns None."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        
        # Also verify that division by non-zero works correctly
        self.assertIsNotNone(self.calc.divide(10, 2))
    
    def test_division_precision(self):
        """Test division with floating point precision."""
        result = self.calc.divide(1, 3)
        self.assertAlmostEqual(result, 0.3333333333333333)
        
        result = self.calc.divide(10, 3)
        self.assertAlmostEqual(result, 3.3333333333333335)


if __name__ == '__main__':
    unittest.main()