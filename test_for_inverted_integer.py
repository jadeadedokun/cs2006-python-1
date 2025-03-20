import unittest
import io
from contextlib import redirect_stdout
from inverted_integer import InvertedInteger

class TestInvertedInteger(unittest.TestCase):
    # Test for creation of object with valid parameters
    def test_successful_creation_of_objects(self):
        x = InvertedInteger(5, 7, 6)
        self.assertEqual(x.object, 5)
        self.assertEqual(x.modulus, 7)
        self.assertEqual(x.multiplier, 6)
        self.assertEqual(str(x), "<5 mod 7 | 6>")

    # Test for creation with multiplier greater than modulus
    def test_creation_with_invalid_multiplier(self):
        x = InvertedInteger(5, 2, 6)
        self.assertEqual(x.object, 1)
        self.assertEqual(x.modulus, 2)
        self.assertEqual(x.multiplier, 0)
        self.assertEqual(str(x), "<1 mod 2 | 0>")

    # Test for creation with object greater than modulus
    def test_creation_with_larger_than_modulus_object(self):
        x = InvertedInteger(5, 2, 1)
        self.assertEqual(x.object, 1)
        self.assertEqual(x.modulus, 2)
        self.assertEqual(x.multiplier, 1)
        self.assertEqual(str(x), "<1 mod 2 | 1>")
    
    # Test for creation with negative modulus
    def test_creation_with_negative_modulus(self):
        with self.assertRaises(ValueError):
            InvertedInteger(5, -2, 1)
            
    # Test for creation with zero modulus
    def test_creation_with_zero_modulus(self):
        with self.assertRaises(ValueError):
            InvertedInteger(5, 0, 1)
            
    # Test for creation with negative object value
    def test_creation_with_negative_values(self):
        x = InvertedInteger(-5, 3, 2)
        self.assertEqual(x.object, 1)
        self.assertEqual(x.modulus, 3)
        self.assertEqual(x.multiplier, 2)
        self.assertEqual(str(x), "<1 mod 3 | 2>")
    
    # Test for creation with large object value
    def test_creation_with_large_values(self):
        x = InvertedInteger(1000000, 7, 3)
        self.assertEqual(x.object, 1)
        self.assertEqual(x.modulus, 7)
        self.assertEqual(x.multiplier, 3)
        self.assertEqual(str(x), "<1 mod 7 | 3>")
    
    # Test for addition of two objects
    def test_addition_normal(self):
        x = InvertedInteger(2, 5, 3)
        y = InvertedInteger(3, 5, 3)
        result = x + y
        self.assertEqual(result.object, 4)
        self.assertEqual(result.modulus, 5)
        self.assertEqual(result.multiplier, 3)
        self.assertEqual(str(result), "<4 mod 5 | 3>")
    
    # Test for addition of an object with itself
    def test_addition_same_object(self):
        x = InvertedInteger(2, 5, 3)
        result = x + x
        self.assertEqual(result.object, 0)
        self.assertEqual(result.modulus, 5)
        self.assertEqual(result.multiplier, 3)
        self.assertEqual(str(result), "<0 mod 5 | 3>")

    # Test for addition with objects having different modulus
    def test_addition_different_modulus(self):
        x = InvertedInteger(2, 5, 3)
        y = InvertedInteger(3, 7, 3)
        with self.assertRaises(ValueError):
            result = x + y
    
    # Test for addition with objects having different multiplier
    def test_addition_different_multiplier(self):
        x = InvertedInteger(2, 5, 3)
        y = InvertedInteger(3, 5, 4)
        with self.assertRaises(ValueError):
            result = x + y
    
    # Test for multiplication of two objects
    def test_multiplication_normal(self):
        x = InvertedInteger(2, 5, 4)
        y = InvertedInteger(3, 5, 4)
        result = x * y
        self.assertEqual(result.object, 1)
        self.assertEqual(result.modulus, 5)
        self.assertEqual(result.multiplier, 4)
        self.assertEqual(str(result), "<1 mod 5 | 4>")
    
    # Test for multiplication of an object with itself
    def test_multiplication_same_object(self):
        x = InvertedInteger(2, 5, 4)
        result = x * x
        self.assertEqual(result.object, 3)
        self.assertEqual(result.modulus, 5)
        self.assertEqual(result.multiplier, 4)
        self.assertEqual(str(result), "<3 mod 5 | 4>")        
    
    # Test for multiplication with objects having different modulus
    def test_multiplication_different_modulus(self):
        x = InvertedInteger(2, 5, 4)
        y = InvertedInteger(3, 7, 4)
        with self.assertRaises(ValueError):
            result = x * y
    
    # Test for multiplication with objects having different multiplier
    def test_multiplication_different_multiplier(self):
        x = InvertedInteger(2, 5, 3)
        y = InvertedInteger(3, 5, 4)
        with self.assertRaises(ValueError):
            result = x * y
    
    # Test for when the modulus is equal to 1
    def test_modulus_one(self):
        x = InvertedInteger(5, 1, 0)
        y = InvertedInteger(10, 1, 0)
        self.assertEqual(x.object, 0)
        self.assertEqual(y.object, 0)
        result_add = x + y
        self.assertEqual(result_add.object, 0)
        self.assertEqual(str(result_add), "<0 mod 1 | 0>")
        result_mult = x * y
        self.assertEqual(result_mult.object, 0)
        self.assertEqual(str(result_mult), "<0 mod 1 | 0>")
    
    # Test for when the multiplier is equal to 0
    def test_multiplier_zero(self):
        x = InvertedInteger(2, 5, 0)
        y = InvertedInteger(3, 5, 0)
        result = x * y
        self.assertEqual(result.object, 0)
        self.assertEqual(str(result), "<0 mod 5 | 0>")
    
    # Test for when the multiplier is equal to 1
    def test_multiplier_one(self):
        x = InvertedInteger(2, 5, 1)
        y = InvertedInteger(3, 5, 1)
        result = x * y
        self.assertEqual(result.object, 4)
        self.assertEqual(str(result), "<4 mod 5 | 1>")
        
    # Test for when the multiplier is equal to modulus - 1
    def test_multiplier_mod_minus_one(self):
        x = InvertedInteger(3, 5, 4)
        y = InvertedInteger(2, 5, 4)
        result = x * y
        self.assertEqual(result.object, 1)
        self.assertEqual(str(result), "<1 mod 5 | 4>")
    
    # Test for when the object is equal to 0
    def test_zero_values(self):
        x = InvertedInteger(0, 5, 3)
        y = InvertedInteger(3, 5, 3)
        add_result = x + y
        self.assertEqual(add_result.object, 2)
        self.assertEqual(str(add_result), "<2 mod 5 | 3>")
        mult_result = x * y
        self.assertEqual(mult_result.object, 3)
        self.assertEqual(str(mult_result), "<3 mod 5 | 3>")
    
    # Test for non-numeric inputs
    def test_non_numeric_inputs(self):
        with self.assertRaises(TypeError):
            InvertedInteger("a", 5, 2)
        with self.assertRaises(TypeError):
            InvertedInteger(5, "b", 2)
        with self.assertRaises(TypeError):
            InvertedInteger(5, 5, "c")
    
    # Test for find_idempotent_pairs function
    def test_find_idempotent_pairs(self):
        x = InvertedInteger(0, 5, 2)
        f = io.StringIO()
        with redirect_stdout(f):
            result = x.find_idempotent_pairs()
        output = f.getvalue()
        
        self.assertIn("These are the pairs for which the law of idempotency holds:", output)
        # Check that the result contains exactly the expected pairs
        expected_pairs = {(1,0), (2,1)}
        self.assertEqual(set(result), expected_pairs)
    
    # Test for find_commutative_pairs function
    def test_find_commutative_pairs(self):
        x = InvertedInteger(0, 5, 2)
        f = io.StringIO()
        with redirect_stdout(f):
            mult_pairs, add_pairs = x.find_commutative_pairs()
        output = f.getvalue()
        
        self.assertIn("The commutative of multiplication holds for values between 1 and 50", output)
        
        self.assertIn("These are the pairs for which commutative addition holds:", output)
        expected_add_pairs = {(1,0), (2,0), (2,1)}
        self.assertEqual(set(add_pairs), expected_add_pairs)

    # Test for find_associative_pairs function
    def test_find_associative_pairs(self):
        x = InvertedInteger(0, 5, 2)
        f = io.StringIO()
        with redirect_stdout(f):
            mult_pairs, add_pairs = x.find_associative_pairs()
        output = f.getvalue()
        
        self.assertIn("The associative of multiplication holds for values between 1 and 20", output)
        
        self.assertIn("These are the pairs for which associative addition holds:", output)
        expected_add_pairs = {(1,0), (2,0), (2,1)}
        self.assertEqual(set(add_pairs), expected_add_pairs)

    # Test for find_right_distributivity_pairs function
    def test_find_right_distributivity_pairs(self):
        x = InvertedInteger(0, 5, 2)
        f = io.StringIO()
        with redirect_stdout(f):
            result = x.find_right_distributivity_pairs()
        output = f.getvalue()
        
        self.assertIn("These are the pairs for which the law of inverted right distributivity holds:", output)
        expected_pairs = {(1,0)}
        self.assertEqual(set(result), expected_pairs)
            
    # Test for _is_same_modulus_and_multiplier method
    def test_is_same_modulus_and_multiplier(self):
        x = InvertedInteger(3, 5, 2)
        y = InvertedInteger(4, 5, 2)
        z = InvertedInteger(3, 6, 2)
        w = InvertedInteger(3, 5, 3)
        
        self.assertTrue(InvertedInteger._is_same_modulus_and_multiplier(x, y))
        
        with self.assertRaises(ValueError):
            InvertedInteger._is_same_modulus_and_multiplier(x, z)
        
        with self.assertRaises(ValueError):
            InvertedInteger._is_same_modulus_and_multiplier(x, w)
    
    # Test for print_values method
    def test_print_values(self):
        f = io.StringIO()
        with redirect_stdout(f):
            InvertedInteger.print_values([(1, 2), (3, 4)])
        output = f.getvalue()
        self.assertIn("(1, 2)", output)
        self.assertIn("(3, 4)", output)

if __name__ == '__main__':
    unittest.main()