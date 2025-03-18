def has_idempotent_property(n, alpha):
    # function check for each value from 0 to the modulus with a fixed multiplier and modulus whether x multiplied by itself gives x
    for x in range(n):
        result = (x + x - alpha * x * x) % n
        if result != x:
            return False
    return True

def has_commutative_multiplication(n, alpha):
    # function to check whether values hold the commutative value of multiplication
    for x in range(n):
        for y in range(n):
            result = (x + y - alpha * x * y) % n
            if result != ((y + x - alpha * y * x) % n):
                return False
    return True

def has_commutative_addition(n, alpha):
    # function to check whether values hold the commutative value of addition
    for x in range(n):
        for y in range(n):
            result = (x - y) % n
            if result != ((y - x) % n):
                return False
    return True

def has_associative_inverted_multiplication(n, alpha):
        #Check if (x ⊗ y) ⊗ z = x ⊗ (y ⊗ z) for all x, y, z ∈ Zn.
    for x in range(n):
        for y in range(n):
            for z in range(n):
                # Compute (x ⊗ y) ⊗ z
                left = (x + y - alpha * x * y) % n
                left = (left + z - alpha * left * z) % n
                
                # Compute x ⊗ (y ⊗ z)
                right = (y + z - alpha * y * z) % n
                right = (x + right - alpha * x * right) % n
                
                if left != right:
                    return False
    return True

def has_associative_inverted_addition(n, alpha):
    #Check if (x ⊕ y) ⊕ z = x ⊕ (y ⊕ z) for all x, y, z ∈ Zn.
    for x in range(n):
        for y in range(n):
            for z in range(n):
                # Compute (x ⊕ y) ⊕ z
                left = (x - y) % n
                left = (left - z) % n
                
                # Compute x ⊕ (y ⊕ z)
                right = (y - z) % n
                right = (x - right) % n
                
                if left != right:
                    return False
    return True

def has_inverted_right_distributivity(n, alpha):
    """Check if (x ⊕ y) ⊗ z = (x ⊗ z) ⊕ (y ⊗ z) for all x, y, z ∈ Zn."""
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