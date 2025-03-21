import algebraic_calculations as ac

class InvertedInteger:
        # function to define the components of the expression
    def __init__(self, obj, modulus, multiplier):
        # ensures that an invalid modulus cannot be used to create an InvertedInteger object
        if modulus <= 0:
            raise ValueError("The modulus must be positive. Please try again.")
        self.modulus = modulus
         # reduces to ensure that both values are part of the set Zn
        self.object = obj % modulus 
        self.multiplier = multiplier % modulus
        
         # function to overwrite "print"
    def __str__(self):
        return f"<{self.object} mod {self.modulus} | {self.multiplier}>"
    
    # function to print relevant pairs from a list
    @staticmethod
    def print_values(list_of_results):
        for result in list_of_results:
            print(result)
        
    # function to check that the modulus is above 0 and an integer
    @staticmethod
    def _is_positive_modulus(variable, other_variable):
        if variable.modulus <= 0 or other_variable.modulus <= 0:
            raise ValueError("The modulus must be a positive integer. Please try again.")
        return True
    

    
    # Analyze pairs (n, alpha) to find those with the most roots of unit
    @staticmethod
    def analyze_inverted_roots_of_unity(max_n=25):
      """Find the maximal number of roots and corresponding (n, α) pairs."""
      max_count = 0
      max_pairs = []
      for n in range(1, max_n + 1):
        for alpha in range(n):
            roots = ac.inverted_roots_of_unity(n, alpha)
            count = len(roots)
            if count > max_count:
                max_count = count
                max_pairs = [(n, alpha, roots)]
            elif count == max_count and count > 0:
                max_pairs.append((n, alpha, roots))
      return max_count, max_pairs

        
    # function to check that both x and y have an identical modulus and multiplier
    @staticmethod
    def _is_same_modulus_and_multiplier(variable, other_variable):
        if not (variable.modulus == other_variable.modulus and variable.multiplier == other_variable.multiplier):
            raise ValueError("The modulus and multiplier of both variables being operated on must be the same.")
        return True
        
    # function to allow the program to support addition
    def __add__(self, other):
        if (self._is_same_modulus_and_multiplier(self, other)):
            result = InvertedInteger(((self.object - other.object) % self.modulus), self.modulus, self.multiplier)
            return result
        return None
        
    # function to allow the program to support multiplication
    def __mul__(self, other):
        if (self._is_same_modulus_and_multiplier(self, other)):
            result = InvertedInteger((self.object + other.object - (self.multiplier * self.object * other.object)) % self.modulus, self.modulus, self.multiplier)
            return result
        return None
        
    def find_pairs(self,modulus,property,checking_function):
        pairs = []
        all_hold = True

        for n in range(1,modulus+1):
            for alpha in range(n):
                if checking_function(n,alpha):
                    pairs.append((n,alpha))
                else: all_hold = False
        if all_hold:
            print(f"The law of {property} holds for values between 1 and {modulus}.")
        else:
            print(f"These are the pairs for which the law of {property} holds:")
            self.print_values(pairs)
            
        return pairs
        
    # helper function to identify pairs that satisfy a specified law
    def find_mult_and_add_pairs(self, modulus, mult_checking_function, add_checking_function,property):
        multiplication_pairs = []
        addition_pairs = []
        mult_all_hold = True
        add_all_hold = True
        checked_pairs = set()

        # loops through from 1 to a specified value to identify which pairs satisfy the condition and adds them to a list
        for n in range(1, modulus+1):
            for alpha in range(n):
                # ensures that pairs will not be re-checked with their reversed order
                if (n, alpha) not in checked_pairs:
                    checked_pairs.add((n,alpha))
                    if mult_checking_function(n,alpha):
                        multiplication_pairs.append((n,alpha))
                    else: mult_all_hold = False
                    if add_checking_function(n,alpha):   
                        addition_pairs.append((n,alpha))
                    else: add_all_hold = False

        # checks whether the law is satisfied for multiplication with all values and outputs specific pairs if not
        if (mult_all_hold):
            print(f"The {property} of multiplication holds for values between 1 and {modulus}.")
        else: 
            print(f"These are the pairs for which {property} multiplication holds:")
            self.print_values(multiplication_pairs)

        # checks whether the law is satisfied for addition with all values and outputs specific pairs if not
        if (add_all_hold):
            print(f"The {property} of addition holds for values between 1 and {modulus}")
        else:
            print(f"These are the pairs for which {property} addition holds:")
            self.print_values(addition_pairs)
                
        return multiplication_pairs, addition_pairs
    
    # function to find idempotent pairs where modulus is between 1 and 50 and the multiplier is less than modulus
    def find_idempotent_pairs(self):
        return self.find_pairs(50,"idempotency",ac.has_idempotent_property)
    
     # function to find commutative pairs (for both operations) where modulus is between 1 and 50 and the multiplier is less than modulus
    def find_commutative_pairs(self):
        return self.find_mult_and_add_pairs(50,ac.has_commutative_multiplication,ac.has_commutative_addition,"commutative")
  
    # function to find associative pairs (for both operations) where modulus is between 1 and 50 and the multiplier is less than modulus
    def find_associative_pairs(self):
        return self.find_mult_and_add_pairs(20,ac.has_associative_inverted_multiplication,ac.has_associative_inverted_addition,"associative")

    """Find all pairs (n, α) where 1 ≤ n ≤ 20 and 0 ≤ α < n, and right distributivity holds."""
    def find_right_distributivity_pairs(self):
            return self.find_pairs(20,"inverted right distributivity",ac.has_inverted_right_distributivity)