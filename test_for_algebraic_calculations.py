import unittest
import algebraic_calculations as ac

class TestAlgebraicCalculations(unittest.TestCase):
    # Test for idempotent property
    def test_has_idempotent_property(self):
        self.assertTrue(ac.has_idempotent_property(1, 0))
        self.assertTrue(ac.has_idempotent_property(2, 1))
        self.assertFalse(ac.has_idempotent_property(3, 1))
        self.assertFalse(ac.has_idempotent_property(3, 0))
        self.assertFalse(ac.has_idempotent_property(4, 2))
    
    # Test for commutative multiplication
    def test_has_commutative_multiplication(self):
        self.assertTrue(ac.has_commutative_multiplication(5, 2))
        self.assertTrue(ac.has_commutative_multiplication(7, 3))
        self.assertTrue(ac.has_commutative_multiplication(1, 0))
        self.assertTrue(ac.has_commutative_multiplication(10, 0))
        self.assertTrue(ac.has_commutative_multiplication(5, 4))
    
    # Test for commutative addition
    def test_has_commutative_addition(self):
        self.assertTrue(ac.has_commutative_addition(1, 0))
        self.assertTrue(ac.has_commutative_addition(2, 0))
        self.assertFalse(ac.has_commutative_addition(3, 0))

    # Test for associative multiplication
    def test_has_associative_inverted_multiplication(self):
        self.assertTrue(ac.has_associative_inverted_multiplication(2, 0))
        self.assertTrue(ac.has_associative_inverted_multiplication(3, 1))
        self.assertTrue(ac.has_associative_inverted_multiplication(1, 0))

    # Test for associative addition
    def test_has_associative_inverted_addition(self):
        self.assertTrue(ac.has_associative_inverted_addition(2, 0))
        self.assertFalse(ac.has_associative_inverted_addition(3, 0))
        self.assertTrue(ac.has_associative_inverted_addition(1, 0))
    
    # Test for right distributivity
    def test_has_inverted_right_distributivity(self):
        self.assertTrue(ac.has_inverted_right_distributivity(1, 0))
        self.assertFalse(ac.has_inverted_right_distributivity(2, 0))
        self.assertFalse(ac.has_inverted_right_distributivity(2, 1))
        self.assertFalse(ac.has_inverted_right_distributivity(3, 2))
        self.assertFalse(ac.has_inverted_right_distributivity(3, 1))

if __name__ == '__main__':
    unittest.main()