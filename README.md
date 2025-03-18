STUDENT ID: 230013682  
CS2006 PRACTICAL 2 README
---------------------------

## Quick Start Guide

This guide will help you get started with exploring inverted integers in Python.

### Dependencies

No external dependencies are required. This module uses only the Python standard library.

### Loading the code

To load the code in a Python interpreter, run the following lines:

```python
from inverted_integer import InvertedInteger
```

## ACTIONS - Creating an Object
### You can create an object by passing a value to be associated with your object, a modulus value and a multiplier value.

For example:

The following line creates an inverted integer with value 3, modulus 7, and multiplier 2
```
x = InvertedInteger(3, 7, 2)
```

The following line creates another inverted integer with value 5, modulus 7, and multiplier 2
```
y = InvertedInteger(5, 7, 2)
```
## ACTIONS - Printing an Object
### You can print your inverted integer objects to see their representation:

For example:

The following line prints the representation of x
```
print(x) 
```
Using the object 'x' above, this line results in the output: **<3 mod 7 | 2 >**

The following line prints the representation of y
```
print(y)  
```
Using the object 'y' above, this line results in the output: **<5 mod 7 | 2 >**

