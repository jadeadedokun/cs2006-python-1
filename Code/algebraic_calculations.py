def has_idempotent_property(n, alpha):
    """
    Function to check for each value from 0 to the modulus with a fixed multiplier and modulus whether x multiplied by itself gives x.
    
    Args:
        n (int): The modulus 
        alpha (int): The multiplier
        
    Returns:
        bool: True if the property holds for all values, False otherwise
        
    Examples:
        >>> has_idempotent_property(1, 0)
        True
        >>> has_idempotent_property(2, 1)
        True
        >>> has_idempotent_property(3, 1)
        False
    """
    for x in range(n):
        result = (x + x - alpha * x * x) % n
        if result != x:
            return False
    return True

def has_commutative_multiplication(n, alpha):
    """
    Function to check whether values hold the commutative value of multiplication.
    
    Args:
        n (int): The modulus
        alpha (int): The multiplier
        
    Returns:
        bool: True if the multiplication is commutative, False otherwise
        
    Examples:
        >>> has_commutative_multiplication(5, 2)
        True
        >>> has_commutative_multiplication(1, 0)
        True
    """
    for x in range(n):
        for y in range(n):
            result = (x + y - alpha * x * y) % n
            if result != ((y + x - alpha * y * x) % n):
                return False
    return True

def has_commutative_addition(n, alpha):
    """
    Function to check whether values hold the commutative value of addition.
    
    Args:
        n (int): The modulus
        alpha (int): The multiplier
        
    Returns:
        bool: True if the addition is commutative, False otherwise
        
    Examples:
        >>> has_commutative_addition(1, 0)
        True
        >>> has_commutative_addition(2, 0)
        True
        >>> has_commutative_addition(3, 0)
        False
    """
    # function to check whether values hold the commutative value of addition
    for x in range(n):
        for y in range(n):
            result = (x - y) % n
            if result != ((y - x) % n):
                return False
    return True

def has_associative_inverted_multiplication(n,alpha):
    """
    Function to perform multiplication and check for associativity.
    
    Args:
        n (int): The modulus
        alpha (int): The multiplier
        
    Returns:
        bool: True if multiplication is associative, False otherwise
        
    Examples:
        >>> has_associative_inverted_multiplication(1, 0)
        True
        >>> has_associative_inverted_multiplication(2, 0)
        True
    """
    # function to perform multiplication and check for associativity
    for x in range(n):
        for y in range(n):
            for z in range(n):
                x_and_y_mult_result = (x + y - alpha * x * y) % n
                result1 = (x_and_y_mult_result + z - alpha * x_and_y_mult_result * z) % n
                
                y_and_z_mult_result = (y + z - alpha * y * z) % n
                result2 = (x + y_and_z_mult_result - alpha * x * y_and_z_mult_result) % n
                
                if result1 != result2:
                    return False
    return True

def has_associative_inverted_addition(n,alpha):
    """
    Function to perform addition and check for associativity.
    
    Args:
        n (int): The modulus
        alpha (int): The multiplier
        
    Returns:
        bool: True if addition is associative, False otherwise
        
    Examples:
        >>> has_associative_inverted_addition(1, 0)
        True
        >>> has_associative_inverted_addition(2, 0)
        True
        >>> has_associative_inverted_addition(3, 0)
        False
    """
    # function to perform addition and check for associativity
    for x in range(n):
        for y in range(n):
            for z in range(n):
                x_and_y_add_result = (x - y) % n
                result1 = (x_and_y_add_result - z) % n
                
                y_and_z_add_result = (y - z) % n
                result2 = (x - y_and_z_add_result) % n
                
                if result1 != result2:
                    return False
    return True

def has_inverted_right_distributivity(n, alpha):
    """
    Check if (x ⊕ y) ⊗ z = (x ⊗ z) ⊕ (y ⊗ z) for all x, y, z ∈ Zn.
    
    Args:
        n (int): The modulus
        alpha (int): The multiplier
        
    Returns:
        bool: True if right distributivity holds, False otherwise
        
    Examples:
        >>> has_inverted_right_distributivity(1, 0)
        True
        >>> has_inverted_right_distributivity(2, 0)
        False
    """
    for x in range(n):
        for y in range(n):
            for z in range(n):
                # Compute (x ⊕ y) ⊗ z
                left_add = (x - y) % n
                left = (left_add + z - alpha * left_add * z) % n
                
                # Compute (x ⊗ z) ⊕ (y ⊗ z)
                right_x = (x + z - alpha * x * z) % n
                right_y = (y + z - alpha * y * z) % n
                right = (right_x - right_y) % n
                
                if left != right:
                    return False
    return True

# Find x in Zn where x⊗x=1 for given n and alpha
def inverted_roots_of_unity(n, alpha):
    """
    Find all x ∈ Zn such that x⊗x = 1.
    
    Args:
        n (int): The modulus
        alpha (int): The multiplier
        
    Returns:
        list: List of values x where x⊗x = 1
        
    Examples:
        >>> inverted_roots_of_unity(1, 0)
        [0]
        >>> inverted_roots_of_unity(2, 1)
        [1]
        >>> inverted_roots_of_unity(5, 2)
        [2, 4]
    """
    roots = []
    target = 1 % n
    for x in range(n):
        result = (2 * x - alpha * x * x) % n
        if result == target:
            roots.append(x)
    return roots