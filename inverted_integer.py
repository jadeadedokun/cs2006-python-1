import algebraic_calculations as ac

class InvertedInteger:
    # function to define the components of the expression
    def __init__(self, obj, modulus, multiplier):
        self.modulus = modulus
        # reduces to ensure that both values are part of the set Zn
        self.object = obj % modulus
        self.multiplier = multiplier % modulus
        
    # function to overwrite "print"
    def __str__(self):
        return "<" + str(self.object) + " mod " + str(self.modulus) + " | " + str(self.multiplier) + " >"
        
    # function to check that the modulus is above 0 and an integer
    @staticmethod
    def _is_positive_modulus(variable, other_variable):
        if variable.modulus <= 0 or other_variable.modulus <= 0:
            raise ValueError("The modulus must be a positive integer. Please try again.")
        return True
        
    # function to check that both x and y have an identical modulus and multiplier
    @staticmethod
    def _is_same_modulus_and_multiplier(variable, other_variable):
        if not (variable.modulus == other_variable.modulus and variable.multiplier == other_variable.multiplier):
            raise ValueError("The modulus and multiplier of both variables being operated on must be the same.")
        return True
        
    # function to allow the program to support addition
    def __add__(self, other):
        if (self._is_positive_modulus(self, other) and self._is_same_modulus_and_multiplier(self, other)):
            result = InvertedInteger(((self.object - other.object) % self.modulus), self.modulus, self.multiplier)
            return result
        return None
        
    # function to allow the program to support multiplication
    def __mul__(self, other):
        if (self._is_positive_modulus(self, other) and self._is_same_modulus_and_multiplier(self, other)):
            result = InvertedInteger((self.object + other.object - (self.multiplier * self.object * other.object)) % self.modulus, self.modulus, self.multiplier)
            return result
        return None
        
    # function to find idempotent pairs where modulus is between 1 and 50 and the multiplier is less than modulus
    def find_idempotent_pairs():
        idempotent_pairs = []
        
        # checks for idempotent pairs between 1 and 50 adds them to a list
        for n in range(1, 51):
            for alpha in range(n):
                if ac.has_idempotent_property(n, alpha):
                    idempotent_pairs.append((n, alpha))
            print("These are the pairs for which idempotency holds:")
            for pair in idempotent_pairs:
                print(pair)
        return idempotent_pairs
    
    # function to find commutative pairs (for both operations) where modulus is between 1 and 50 and the multiplier is less than modulus
    def find_commutative_pairs():
        mult_non_commutative_pairs = []
        add_non_commutative_pairs = []

        # checks for commutative pairs between 1 and 50 using both multiplication and addition
        for n in range(1, 51):
            for alpha in range(n):
                if not ac.has_commutative_multiplication(n, alpha):
                    mult_non_commutative_pairs.append((n, alpha))
                if not ac.has_commutative_addition(n, alpha):
                    add_non_commutative_pairs.append((n, alpha))
                    
        if not mult_non_commutative_pairs:
            print("All pairs between 1 and 50 hold the commutative property of multiplication.")
        else:
            print("These are the non-commutative multiplication pairs:")
            for pair in mult_non_commutative_pairs:
                print(pair)
                
        if not add_non_commutative_pairs:
            print("All pairs between 1 and 50 hold the commutative property of addition.")
        else:
            print("These are the non-commutative addition pairs:")
            for pair in add_non_commutative_pairs:
                print(pair)
                
        return mult_non_commutative_pairs, add_non_commutative_pairs

    # function to find associative pairs (for both operations) where modulus is between 1 and 50 and the multiplier is less than modulus
    def find_associative_pairs():
        associative_pairs = []
        
        # checks for associative pairs between 1 and 50 adds them to a list
        for n in range(1, 51):
            for alpha in range(n):
                if ac.has_associative_inverted_multiplication(n, alpha):
                    associative_pairs.append((n, alpha))
            print("These are the pairs for which associativity holds:")
            for pair in associative_pairs:
                print(pair)
        return associative_pairs