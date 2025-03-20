#!/bin/bash 
# 230013682

pip3 install coverage
from inverted_integer import InvertedInteger

python3 test_for_algebraic_calculations.py
python3 test_for_inverted_integer.py
python3 test_for_inverted_integers.py

coverage report