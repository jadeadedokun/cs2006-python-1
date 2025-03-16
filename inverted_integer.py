class InvertedInteger:
    # function to define the components of the expression
    def __init__(self, obj, modulus, multiplier):
        self.object = obj
        self.modulus = modulus
        self.multiplier = multiplier
        
    # function to overwrite "print"
    def __str__(self):
        return "<" + str(self.object) + " mod " + str(self.modulus) + " | " + str(self.multiplier) + " >"
        
    # function to check that the modulus is above 0 and an integer
    @staticmethod
    def __is_positive_modulus__(variable, other_variable):
        if variable.modulus <= 0 or other_variable.modulus <= 0:
            raise ValueError("The modulus must be a positive integer. Please try again.")
        return True
        
    # function to check that x and y come from the set Zn (where n is modulus, so the set is 0 to modulus - 1)
    @staticmethod
    def __is_valid_variable__(variable, other_variable):
        # ensures that neither x nor y's modulus is invalid
        if not ((0 <= variable.object < variable.modulus) and (0 <= variable.multiplier < variable.modulus)):
            if not ((0 <= other_variable.object < other_variable.modulus) and (0 <= other_variable.multiplier < other_variable.modulus)):
                raise ValueError("This is not a valid variable. Please try again.")
        return True
        
    # function to check that both x and y have an identical modulus and multiplier
    @staticmethod
    def __is_same_modulus_and_multiplier__(variable, other_variable):
        if not (variable.modulus == other_variable.modulus and variable.multiplier == other_variable.multiplier):
            raise ValueError("The modulus and multiplier of both variables being operated on must be the same.")
        return True
        
    # function to allow the program to support addition
    def __add__(self, other):
        result = -1
        if (self.__is_valid_variable__(self, other) and self.__is_positive_modulus__(self, other) and self.__is_same_modulus_and_multiplier__(self, other)):
            result = InvertedInteger(((self.object - other.object) % self.modulus), self.modulus, self.multiplier)
        return result
        
    # function to allow the program to support multiplication
    def __mul__(self, other):
        result = -1
        # ensures that all variable, modulus and multiplier conditions are met before attempting multiplication
        if (self.__is_valid_variable__(self, other) and self.__is_positive_modulus__(self, other) and self.__is_same_modulus_and_multiplier__(self, other)):
            result = InvertedInteger((self.object + other.object - (self.multiplier * self.object * other.object)) % self.modulus, self.modulus, self.multiplier)
        return result
        
    # function check for each value from 0 to the modulus with a fixed multiplier and modulus whether x multiplied by itself gives x
    @staticmethod
    def __has_all_idempotents_property__(n, alpha):
        for x in range(n):
            result = (x + x - alpha * x * x) % n
            if result != x:
                return False
        return True
        
    # function to find idempotent pairs where modulus is between 1 and 50 and the multiplier is less than modulus
    def find_idempotent_pairs(self):
        # establishes a store for pairs that match the specified condition and adds them into it
        idempotent_pairs = []
        
        # checks for idempotent pairs between 1 and 50 adds them to a list
        for i in range(1, 51):
            for j in range(0, i):
                if self.__has_all_idempotents_property__(i, j):
                    idempotent_pairs.append((i, j))
        return idempotent_pairs
    
    # function to check whether values hold the commutative value of multiplication
    @staticmethod
    def __has_commutative_inverted_multiplication__(n, alpha):
        for x in range(n):
            for y in range(n):
                result = (x + y - alpha * x * y) % n
                if result != ((y + x - alpha * y * x) % n):
                    return False
        return True

    # function to check whether values hold the commutative value of addition
    @staticmethod
    def __has_commutative_inverted_addition__(n, alpha):
        for x in range(n):
            for y in range(n):
                    result = (x - y) % n
                    if result != ((y - x) % n):
                        return False
        return True
    
    # function to find commutative pairs (for both operations) where modulus is between 1 and 50 and the multiplier is less than modulus
    def find_commutative_pairs(self):
        mult_non_commutative_pairs = []
        add_non_commutative_pairs = []

        # checks for commutative pairs between 1 and 50 using both multiplication and addition
        for i in range(1, 51):
            for j in range(0, i):
                if not self.__has_commutative_inverted_multiplication__(i, j):
                    mult_non_commutative_pairs.append((i, j))
                if not self.__has_commutative_inverted_addition__(i, j):
                    add_non_commutative_pairs.append((i, j))
                    
        if not mult_non_commutative_pairs:
            print("All pairs between 1 and 50 hold the commutative property of multiplication.")
        if not add_non_commutative_pairs:
            print("All pairs between 1 and 50 hold the commutative property of addition.")
                
        return mult_non_commutative_pairs, add_non_commutative_pairs