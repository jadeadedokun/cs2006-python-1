from inverted_integer import InvertedInteger

class InvertedIntegers:
    def __init__(self, modulus: int, alpha:int):
        #initialise with modules(must be positive) and alpha (mod modules). 
        if modulus <= 0:
          raise ValueError("Modulus must be positive. For n=1, use modulus=1.")
        self.modulus = modulus
        self.alpha = alpha % modulus
    
    def __str__(self):
        #string representation of the object
        return f"<Zn mod {self.modulus} | alpha={self.alpha}>"
    
    def size(self):
        #returns size of the set (equal to the modules)
        return self.modulus
  
    def __iter__(self):
       #iterate over all elements in the set yielding InvertedInteger objects 
        for x in range(self.modulus):
            yield InvertedInteger(x, self.modulus, self.alpha)