"""
Euclid.py
given two divisors (x and y)
if x < y, swap x and y
while y is not zero
  remainder = x mod y
  x = y
  y = remainder
  
"""
import pdb

def gcd(x, y):
    rem = 999
    #pdb.set_trace()
    if x < y:
        (x, y) = (y, x)
    
    while (y != 0):
        rem = x % y
        x = y
        y = rem
        
    return rem

print gcd(54, 24)
