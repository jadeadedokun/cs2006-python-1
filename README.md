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

## Actions - Creating an Object
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
## Actions - Printing an Object
### You can print your inverted integer objects to see their representation.

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

## Actions - Multiplying Objects
### You can multiply your inverted integer objects to get a resulting value.

For example:

The following line multiplies the previously created x and y object by each other and prints the resulting value
```
print(x * y)
```

## Actions - Adding Objects
### You can add your inverted integer objects together to get a resulting value.

For example:

The following line adds the previously created x and y object together and prints the resulting value
```
print(x + y)
```

## Actions - Determining Idempotency
### You can find out whether the idempotency law holds for all pairs (n,a) where n is the modulus and a is the multplier of pairs between 1 - 50, and if not which pairs it **does** hold for.

For example: 

The following line uses the previously created x object to call the function for determining idempotent pairs
```
x.find_idempotent_pairs()
```


## Actions - Determining Commutativity
### You can find out whether the commutativity law holds for all added pairs (n,a) where n is the modulus and a is the multplier of pairs between 1 - 50, and if not which pairs it **does** hold for.

For example: 

The following line uses the previously created x object to call the function for determining commutative pairs
```
x.find_commutative_pairs()
```


## Actions - Determining Associativity
### You can find out whether the associativity law holds for all added and multiplied pairs (n,a) where n is the modulus and a is the multplier of pairs between 1 - 20, and if not which pairs it **does** hold for.

For example: 

The following line uses the previously created x object to call the function for determining associative pairs
```
x.find_associative_pairs()
```

## Actions - Determining Inverted Right Distributivity
### You can find out whether the inverted right distributivity law holds for all pairs (n,a) where n is the modulus and a is the multplier of pairs between 1 - 20, and if not which pairs it **does** hold for.

For example: 

The following line uses the previously created x object to call the function for determining inverted right distributivity pairs
```
x.find_right_distributivity_pairs()
```
