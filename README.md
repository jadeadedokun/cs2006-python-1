STUDENT ID: 230013682  
CS2006 PRACTICAL 2 README
---------------------------

## Quick Start Guide

This guide will help you get started with exploring inverted integers in Python.

### Dependencies

Apart from the Python standard library, this program requires for coverage to be installed for unit tests by running the following line on the terminal:
```
pip3 install coverage
```

### Loading the code

To load the code in a Python interpreter, run the following line:

```python
python3 -i -c "from inverted_integer import InvertedInteger, InvertedIntegers; print('Python interpreter started with InvertedInteger and InvertedIntegers imported.')"
```

## Actions - Creating an Object
### You can create an object by passing a value to be associated with your object, a modulus value and a multiplier value.

For example:

The following line creates an inverted integer with value 3, modulus 7, and multiplier 2
```python
x = InvertedInteger(3, 7, 2)
```

The following line creates another inverted integer with value 5, modulus 7, and multiplier 2
```python
y = InvertedInteger(5, 7, 2)
```
## Actions - Printing an Object
### You can print your inverted integer objects to see their representation.

For example:

The following line prints the representation of x
```python
print(x) 
```
Using the object 'x' above, this line results in the output: **<3 mod 7 | 2 >**

The following line prints the representation of y
```python
print(y)  
```
Using the object 'y' above, this line results in the output: **<5 mod 7 | 2 >**

## Actions - Multiplying Objects
### You can multiply your inverted integer objects to get a resulting value.

For example:

The following line multiplies the previously created x and y object by each other and prints the resulting value
```python
print(x * y)
```

## Actions - Adding Objects
### You can add your inverted integer objects together to get a resulting value.

For example:

The following line adds the previously created x and y object together and prints the resulting value
```python
print(x + y)
```

## Actions - Determining Idempotency
### You can find out whether the idempotency law holds for all pairs (n,a) where n is the modulus and a is the multplier of pairs between 1 - 50, and if not which pairs it **does** hold for.

For example: 

The following line uses the previously created x object to call the function for determining idempotent pairs
```python
x.find_idempotent_pairs()
```


## Actions - Determining Commutativity
### You can find out whether the commutativity law holds for all added pairs (n,a) where n is the modulus and a is the multplier of pairs between 1 - 50, and if not which pairs it **does** hold for.

For example: 

The following line uses the previously created x object to call the function for determining commutative pairs
```python
x.find_commutative_pairs()
```


## Actions - Determining Associativity
### You can find out whether the associativity law holds for all added and multiplied pairs (n,a) where n is the modulus and a is the multplier of pairs between 1 - 20, and if not which pairs it **does** hold for.

For example: 

The following line uses the previously created x object to call the function for determining associative pairs
```python
x.find_associative_pairs()
```

## Actions - Determining Inverted Right Distributivity
### You can find out whether the inverted right distributivity law holds for all pairs (n,a) where n is the modulus and a is the multplier of pairs between 1 - 20, and if not which pairs it **does** hold for.

For example: 

The following line uses the previously created x object to call the function for determining inverted right distributivity pairs
```python
x.find_right_distributivity_pairs()
```

## Actions - Creating and Using InvertedIntegers
### You can create an InvertedIntegers object that represents the entire set Zn with a specific modulus and multiplier.

For example:

The following line creates an InvertedIntegers object with modulus 5 and multiplier 2
```python
integers = InvertedIntegers(5, 2)
```
As above, you can print your InvertedIntegers objects to see their representation.

For example:

The following line prints the representation of the **x** object:
```python
print(integers)
```
Using the object 'integers' above, this line results in the output: **<Zn mod 5 | 2 >**

## Actions - Getting the size of the set
### You can determine how many elements are in the set using the size method:

```python
integers.size()
print(size)
```
Using the object 'integers' above, this line results in the output: **5**

## Actions - Iterating through all elements
### You can iterate through all elements in the set Zn:

```python
for x in integers:
    print(x)
```
This will print:
<0 mod 5 | 2>
<1 mod 5 | 2>
<2 mod 5 | 2>
<3 mod 5 | 2>
<4 mod 5 | 2>

## Actions - Running Tests
### You can run unit tests to verify that the implementation works correctly.

To run the tests with coverage and also the doctests (for each individual file) from the command line:
```bash
./runTestsWithCoverage.sh
```