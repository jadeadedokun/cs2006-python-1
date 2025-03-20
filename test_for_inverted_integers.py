import unittest
from inverted_integer import InvertedIntegers

class TestInvertedIntegers(unittest.TestCase):
    # Test for creation of InvertedIntegers object
    def test_creation(self):
        integers = InvertedIntegers(5, 2)
        self.assertEqual(integers.modulus, 5)
        self.assertEqual(integers.alpha, 2)
    
    # Test for creation with negative modulus
    def test_creation_with_negative_modulus(self):
        with self.assertRaises(ValueError):
            InvertedIntegers(-5, 2)
    
    # Test for creation with zero modulus
    def test_creation_with_zero_modulus(self):
        with self.assertRaises(ValueError):
            InvertedIntegers(0, 2)
    
    # Test for string representation
    def test_str(self):
        integers = InvertedIntegers(5, 2)
        self.assertEqual(str(integers), "<Zn mod 5 | alpha=2>")
    
    # Test for size method
    def test_size(self):
        integers = InvertedIntegers(5, 2)
        self.assertEqual(integers.size(), 5)
    
    # Test for iteration
    def test_iteration(self):
        integers = InvertedIntegers(3, 2)
        elements = list(integers)
        self.assertEqual(len(elements), 3)
        
        self.assertEqual(elements[0].object, 0)
        self.assertEqual(elements[0].modulus, 3)
        self.assertEqual(elements[0].multiplier, 2)
        
        self.assertEqual(elements[1].object, 1)
        self.assertEqual(elements[1].modulus, 3)
        self.assertEqual(elements[1].multiplier, 2)
        
        self.assertEqual(elements[2].object, 2)
        self.assertEqual(elements[2].modulus, 3)
        self.assertEqual(elements[2].multiplier, 2)
    
    # Test for very large modulus
    def test_large_modulus(self):
        integers = InvertedIntegers(1000, 5)
        self.assertEqual(integers.size(), 1000)
        
        iterator = iter(integers)
        first = next(iterator)
        self.assertEqual(first.object, 0)
        self.assertEqual(first.modulus, 1000)
        self.assertEqual(first.multiplier, 5)
    
    # Test for non-numeric inputs
    def test_non_numeric_inputs(self):
        with self.assertRaises(TypeError):
            InvertedIntegers("a", 2)
        with self.assertRaises(TypeError):
            InvertedIntegers(5, "b")

if __name__ == '__main__':
    unittest.main()