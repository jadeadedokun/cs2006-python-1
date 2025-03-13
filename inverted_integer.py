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
      def __is_valid_variable__(variable,other_variable):
        # ensures that neither x nor y's modulus is invalid
        if not ((0 <= variable.object < variable.modulus) and (0 <= variable.multiplier < variable.modulus)):
            if not ((0 <= other_variable.object < other_variable.modulus) and (0 <= other_variable.multiplier < other_variable.modulus)):
                  raise ValueError("This is not a valid variable. Please try again.")
        return True


            # function to check that both x and y have an identical modulus and multiplier
      @staticmethod
      def __defined_for_same_values__(variable, other_variable):
            if not (variable.modulus == other_variable.modulus and variable.multiplier == other_variable.multiplier):
                 raise ValueError("The modulus and multiplier of both variables being operated on must be the same.")
            return True

#
            # function to allow the program to support addition
      def __add__(self,other):
            result = -1
            if (self.__is_valid_variable__(self,other) and self.__is_positive_modulus__(self,other) and self.__defined_for_same_values__(self, other)):
                  result = InvertedInteger(((self.object - other.object) % self.modulus),self.modulus,self.multiplier)
            return result
      
 
            # function to allow the program to support multiplication
      def __mul__(self,other):
            result = -1
            if (self.__is_valid_variable__(self,other) and self.__is_positive_modulus__(self,other) and self.__defined_for_same_values__(self, other)):
                  result = InvertedInteger(self.object
                                              + other.object - (self.multiplier
                                              * (self.object * other.object) % self.modulus),self.modulus,self.multiplier)
            return result