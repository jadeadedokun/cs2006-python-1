import algebraic_calculations as ac

class InvertedInteger:
    """
    A class that defines the components of an inverted integer expression with the specified modulus and multiplier.
    
    Examples:
        >>> x = InvertedInteger(5, 7, 6)
        >>> str(x)
        '<5 mod 7 | 6>'
        >>> y = InvertedInteger(3, 7, 6)
        >>> z = x + y
        >>> str(z)
        '<2 mod 7 | 6>'
        >>> w = x * y
        >>> str(w)
        '<2 mod 7 | 6>'
    """

    def __init__(self, obj, modulus, multiplier):
        """
        Function to define the components of the expression and ensure that invalid modulus values cannot be used.
        
        Args:
            obj (int): The object value
            modulus (int): The modulus value, must be positive
            multiplier (int): The multiplier value
            
        Raises:
            ValueError: If modulus is not positive
            
        Examples:
            >>> x = InvertedInteger(5, 7, 6)
            >>> x.object
            5
            >>> x.modulus
            7
            >>> x.multiplier
            6
        """
        # ensures that an invalid modulus cannot be used to create an InvertedInteger object
        if modulus <= 0:
            raise ValueError("The modulus must be positive. Please try again.")
        self.modulus = modulus
         # reduces to ensure that both values are part of the set Zn
        self.object = obj % modulus 
        self.multiplier = multiplier % modulus
        
    def __str__(self):
        """
        Function to overwrite "print".
        
        Returns:
            str: A string representation of the inverted integer
            
        Examples:
            >>> str(InvertedInteger(5, 7, 6))
            '<5 mod 7 | 6>'
        """
        return f"<{self.object} mod {self.modulus} | {self.multiplier}>"
    
    @staticmethod
    def print_values(list_of_results):
        """
        Function to print relevant pairs from a list for clearer output.
        
        Args:
            list_of_results: List of values to print
        """
        for result in list_of_results:
            print(result)
    
    @staticmethod
    def analyze_inverted_roots_of_unity(max_n=25):
        """
        Function to find the largest number of roots and corresponding (n, α) pairs.
        
        Args:
            max_n (int): Maximum value of n to check
            
        Returns:
            tuple: (max_count, max_pairs) where max_count is the maximum number of roots
                  and max_pairs is a list of (n, alpha, roots) tuples
        """
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

        
    @staticmethod
    def _is_same_modulus_and_multiplier(variable, other_variable):
        """
        Function to check that both x and y have an identical modulus and multiplier to ensure valid operations.
        
        Args:
            variable: First InvertedInteger object
            other_variable: Second InvertedInteger object
            
        Returns:
            bool: True if they have the same modulus and multiplier
            
        Raises:
            ValueError: If they don't have the same modulus and multiplier
        """
        if not (variable.modulus == other_variable.modulus and variable.multiplier == other_variable.multiplier):
            raise ValueError("The modulus and multiplier of both variables being operated on must be the same.")
        return True
        
    def __add__(self, other):
        """
        Function to allow the program to support addition between two InvertedInteger objects.
        
        Args:
            other: InvertedInteger object to add
            
        Returns:
            InvertedInteger: Result of addition
            
        Examples:
            >>> x = InvertedInteger(2, 5, 3)
            >>> y = InvertedInteger(3, 5, 3)
            >>> z = x + y
            >>> z.object
            4
        """
        # ensures that modulus and multiplier have to be the same for addition to be performed
        if (self._is_same_modulus_and_multiplier(self, other)):
            result = InvertedInteger(((self.object - other.object) % self.modulus), self.modulus, self.multiplier)
            return result
        return None
        
    def __mul__(self, other):
        """
        Function to allow the program to support multiplication between two InvertedInteger objects.
        
        Args:
            other: InvertedInteger object to multiply
            
        Returns:
            InvertedInteger: Result of multiplication
            
        Examples:
            >>> x = InvertedInteger(2, 5, 4)
            >>> y = InvertedInteger(3, 5, 4)
            >>> z = x * y
            >>> z.object
            1
        """
        # ensures that modulus and multiplier have to be the same for multiplication to be performed
        if (self._is_same_modulus_and_multiplier(self, other)):
            result = InvertedInteger((self.object + other.object - (self.multiplier * self.object * other.object)) % self.modulus, self.modulus, self.multiplier)
            return result
        return None
        
    def find_pairs(self,modulus,property,checking_function):
        """
        Function to loop through from 1 to a specified value to identify which pairs satisfy the condition and add them to a list.
        
        Args:
            modulus (int): Maximum value of n to check
            property (str): Name of the property being checked
            checking_function: Function that checks if a pair satisfies the property
            
        Returns:
            list: List of pairs (n,alpha) that satisfy the property
        """
        pairs = []
        all_hold = True

        for n in range(1,modulus+1):
            for alpha in range(n):
                if checking_function(n,alpha):
                    pairs.append((n,alpha))
                else: all_hold = False
        # checks whether the law is satisfied for all values and outputs specific pairs if not
        if all_hold:
            print(f"The law of {property} holds for values between 1 and {modulus}.")
        else:
            print(f"These are the pairs for which the law of {property} holds:")
            self.print_values(pairs)
            
        return pairs
        
    def find_mult_and_add_pairs(self, modulus, mult_checking_function, add_checking_function,property):
        """
        Helper function to identify pairs that satisfy a specified law for both multiplication and addition operations.
        
        Args:
            modulus (int): Maximum value of n to check
            mult_checking_function: Function that checks if a pair satisfies the property for multiplication
            add_checking_function: Function that checks if a pair satisfies the property for addition
            property (str): Name of the property being checked
            
        Returns:
            tuple: (multiplication_pairs, addition_pairs) where each is a list of pairs (n,alpha)
        """
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
    
    def find_idempotent_pairs(self):
        """
        Function to find idempotent pairs where modulus is between 1 and 50 and the multiplier is less than modulus.
        
        Returns:
            list: List of pairs (n,alpha) where the idempotent property holds
            
        Examples:
            >>> pairs = InvertedInteger(0, 5, 2).find_idempotent_pairs()
            These are the pairs for which the law of idempotency holds:
            (1, 0)
            (2, 1)
        """
        return self.find_pairs(50,"idempotency",ac.has_idempotent_property)
    
    def find_commutative_pairs(self):
        """
        Function to find commutative pairs (for both operations) where modulus is between 1 and 50 and the multiplier is less than modulus.
        
        Returns:
            tuple: (multiplication_pairs, addition_pairs) where each is a list of pairs (n,alpha)
        """
        return self.find_mult_and_add_pairs(50,ac.has_commutative_multiplication,ac.has_commutative_addition,"commutative")
  
    def find_associative_pairs(self):
        """
        Function to find associative pairs (for both operations) where modulus is between 1 and 20 and the multiplier is less than modulus.
        
        Returns:
            tuple: (multiplication_pairs, addition_pairs) where each is a list of pairs (n,alpha)
        """
        return self.find_mult_and_add_pairs(20,ac.has_associative_inverted_multiplication,ac.has_associative_inverted_addition,"associative")

    """Find all pairs (n, α) where 1 ≤ n ≤ 20 and 0 ≤ α < n, and right distributivity holds."""
    def find_right_distributivity_pairs(self):
        """
        Function to find all pairs (n, α) where 1 ≤ n ≤ 20 and 0 ≤ α < n, and right distributivity holds.
        
        Returns:
            list: List of pairs (n,alpha) where right distributivity holds
        """
        return self.find_pairs(20,"inverted right distributivity",ac.has_inverted_right_distributivity)