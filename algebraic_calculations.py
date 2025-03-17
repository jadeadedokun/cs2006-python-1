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

def has_associative_inverted_multiplication(n,alpha):
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