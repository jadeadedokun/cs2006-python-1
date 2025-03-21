from inverted_integer import InvertedInteger

class InvertedIntegers:
    def __init__(self, modulus, alpha):
        if modulus <= 0:
            raise ValueError("Modulus must be positive.")
        self.modulus = modulus
        self.alpha = alpha % modulus
    
    def __str__(self):
        return f"<Zn mod {self.modulus} | alpha={self.alpha}>"
    
    def size(self):
        return self.modulus
    
    def __iter__(self):
        for x in range(self.modulus):
            yield InvertedInteger(x, self.modulus, self.alpha)