from inverted_integer import InvertedInteger

class InvertedIntegers:
    def __init__(self, modulus: int, alpha:int):
        """
        Initialize an InvertedIntegers object with the specified modulus and alpha.
        
        Args:
            modulus (int): The modulus value (must be positive)
            alpha (int): The multiplier value (reduced automatically by modulus)
            
        Raises:
            ValueError: If modulus isn't positive
            
        Examples:
            >>> integers = InvertedIntegers(5, 2)
            >>> integers.modulus
            5
            >>> integers.alpha
            2
        """
        # initialise with modules(must be positive) and alpha (mod modules)
        if modulus <= 0:
          raise ValueError("Modulus must be positive. For n=1, use modulus=1.")
        self.modulus = modulus
        self.alpha = alpha % modulus
        
    def __str__(self):
        """
        Overwrite the print function to provide a clear representation of set parameters.
        
        Returns:
            str: A formatted string showing the modulus and alpha
            
        Examples:
            >>> str(InvertedIntegers(5, 2))
            '<Zn mod 5 | alpha=2>'
        """
        # string representation of the object
        return f"<Zn mod {self.modulus} | alpha={self.alpha}>"
        
    def size(self):
        """
        Return the size of the set which is equal to the modulus.
        
        Returns:
            int: The modulus value
            
        Examples:
            >>> InvertedIntegers(5, 2).size()
            5
        """
        # returns size of the set (equal to the modules)
        return self.modulus
        
    def __iter__(self):
        """
        Yield elements on-the-fly instead of storing a list to optimise memory usage.
        
        Yields:
            InvertedInteger: Each element in the set from 0 to modulus-1
            
        Examples:
            >>> list(InvertedIntegers(2, 1))[0].object
            0
            >>> list(InvertedIntegers(2, 1))[1].object
            1
        """
        # iterate over all elements in the set yielding InvertedInteger objects 
        for x in range(self.modulus):
            yield InvertedInteger(x, self.modulus, self.alpha)