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
      def __is_positive_modulus__(variable):
        if variable.modulus <= 0:
            raise ValueError("The modulus must be a positive integer. Please try again.")
        return True


            # function to check that x and y come from the set Zn (where n is modulus, so the set is 0 to modulus - 1)
      @staticmethod
      def __is_valid_variable__(variable):
        # should check in one go that both the multiplier AND x and y are more than 0 positive numbers in thse set!!!
        if not ((0 <= variable.object < variable.modulus) and (0 <= variable.multiplier < variable.modulus)):
            raise ValueError("This is not a valid variable. Please try again.")
        return True


            # function to allow the program to support addition
      def __add__(self,other):
            result = -1
            if (self.__is_valid_variable__(self) and self.__is_valid_variable__(other) and self.__is_positive_modulus__(self) and self.__is_positive_modulus__(other)):
                  result = InvertedInteger(((self.object - other.object) % self.modulus),self.modulus,self.multiplier)
            return result
      
 
            # function to allow the program to support multiplication
      def __mul__(self,other):
            result = -1
            if (self.__is_valid_variable__(self) and self.__is_valid_variable__(other) and self.__is_positive_modulus__(self) and self.__is_positive_modulus__(other)):
                  result = InvertedInteger(self.object
                                              + other.object - (self.multiplier
                                              * (self.object * other.object) % self.modulus),self.modulus,self.multiplier)
            return result