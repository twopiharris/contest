""" plus and minus 
    each input is two integers
    integers are the sum and difference
    of two integers
"""

data = ((45, 5), 
        (8, 3), 
        (12, 0), 
        (11, 11), 
        (44, 5))
        
def getB(sum, diff):
    b = (sum - diff)/2
    if b == (sum - diff)/2.0:
        result = b
    else:
        result = -1
    return result
    
def getA(sum, b):
    a = sum - b
    return a
    
for problem in data:
    (sum, diff) = problem
    b = getB(sum, diff)
    if b == -1:
        print "no solution"
    else:
        a = getA(sum, b)
        #print "sum and difference of %d and %d" % (a, b)
        print a, b