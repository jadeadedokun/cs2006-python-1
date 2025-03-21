#!/bin/bash
# 230013682

# Installs coverage
pip3 install coverage

# Runs specific unit tests with coverage
coverage run -m unittest test_for_algebraic_calculations.py test_for_inverted_integer.py test_for_inverted_integers.py test_for_inverted_roots_of_unity.py

# Generates a coverage report
coverage report test_for_algebraic_calculations.py test_for_inverted_integer.py test_for_inverted_integers.py test_for_inverted_roots_of_unity.py

# Individually performs docutests on each file
echo "Testing algebraic_calculations.py..."
python3 -m doctest -v algebraic_calculations.py

echo "Testing inverted_integer.py..."
python3 -m doctest -v inverted_integer.py

echo "Testing inverted_integers.py..."
python3 -m doctest -v inverted_integers.py

echo "The doctests have been run successfully."