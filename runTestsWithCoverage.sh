#!/bin/bash
# 230013682

# Installs coverage
pip3 install coverage

# Runs specific unit tests with coverage
coverage run -m unittest test_for_algebraic_calculations.py test_for_inverted_integer.py test_for_inverted_integers.py test_for_inverted_roots_of_unity.py

# Generates a coverage report
coverage report