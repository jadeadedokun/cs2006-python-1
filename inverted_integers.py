from inverted_integer import InvertedInteger

class InvertedIntegers:
    def __init__(self, modulus: int, alpha:int):
        if modulus <= 0:
          raise ValueError("Modulus must be positive. For n=1, use modulus=1.")
        self.modulus = modulus
        self.alpha = alpha % modulus
    
    def __str__(self):
        return f"<Zn mod {self.modulus} | alpha={self.alpha}>"
    
    def size(self):
        return self.modulus
  
    def __iter__(self):
        """Yield elements on-the-fly instead of storing a list."""
        for x in range(self.modulus):
            yield InvertedInteger(x, self.modulus, self.alpha)