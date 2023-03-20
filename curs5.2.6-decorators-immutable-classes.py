from dataclasses import dataclass

@dataclass(frozen=True)
class MathValues:
    pi = 3.1415926535
    phi = 1.618033988


math = MathValues()
print(math.pi) 
print(math.phi) 

# Setarea unei functii nu mai functioneaza daca frozen este true
math.pi = 3.14
print(math.pi) 

