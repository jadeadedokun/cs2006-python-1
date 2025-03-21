
# Test script
from algebraic_calculations import has_inverted_right_distributivity
from inverted_integer import InvertedInteger, InvertedIntegers

# Test right distributivity function
print("Testing right distributivity function:")
print(has_inverted_right_distributivity(1, 0))  # True
print(has_inverted_right_distributivity(2, 1))  # True
print(has_inverted_right_distributivity(3, 2))  # False

# Test find_right_distributivity_pairs method
x = InvertedInteger(3, 7, 2)
print("\nRight distributivity pairs:", x.find_right_distributivity_pairs())

# Test InvertedIntegers class
zn = InvertedIntegers(5, 2)
print("\nInvertedIntegers instance:", zn)
print("Size of Zn:", zn.size())

# Test iteration over InvertedIntegers
print("\nIterating over Zn:")
for x in zn:
    print(x)

    print("\nTesting combinations of n and alpha for right distributivity:")
for n in range(2, 20):
    for alpha in range(1, n):
        result = has_inverted_right_distributivity(n, alpha)
        print(f"Distributivity for n={n}, alpha={alpha}: {result}")


