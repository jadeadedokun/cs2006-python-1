import unittest
import algebraic_calculations as ac
from inverted_integer import InvertedInteger

class TestInvertedRootsOfUnity(unittest.TestCase):
    def test_n1_alpha0(self):
       roots = ac.inverted_roots_of_unity(1, 0)
       self.assertEqual(roots, [0])

    def test_n2_alpha1(self):
        roots = ac.inverted_roots_of_unity(2, 1)
        self.assertEqual(roots, [1])

    def test_n3_alpha2(self):
        roots = ac.inverted_roots_of_unity(3, 2)
        self.assertEqual(roots, [])

    def test_n5_alpha2(self):
        roots = ac.inverted_roots_of_unity(5, 2)
        self.assertEqual(roots, [2, 4])
 
    def test_n7_alpha3(self):
        roots = ac.inverted_roots_of_unity(7, 3)
        self.assertEqual(roots, [])

    def test_n10_alpha4(self):
        roots = ac.inverted_roots_of_unity(10, 4)
        self.assertEqual(roots, [])
    def test_n15_alpha1(self):
        roots = ac.inverted_roots_of_unity(15, 1)
        self.assertEqual(roots, [1])  # Only x=1 is valid

    def test_n21_alpha1(self):
        roots = ac.inverted_roots_of_unity(21, 1)
        self.assertEqual(roots, [1])  # Only x=1 is valid

    def test_analyze_max_roots(self):
         max_count, max_pairs = InvertedInteger.analyze_inverted_roots_of_unity(max_n=25)
    
         # Check for the correct maximal pair (n=25, α=1)
         found_25_1 = any(n == 25 and alpha == 1 for n, alpha, _ in max_pairs)
         self.assertTrue(found_25_1, "Pair (n=25, α=1) not found in maximal roots.")
         self.assertEqual(max_count, 5, "Maximal roots should be 5.")
   
if __name__ == "__main__":
         
         print(ac.inverted_roots_of_unity(25, 1))

         unittest.main()