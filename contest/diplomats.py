""" diplomats """

import pdb
import random

"""
n = 11

enemies = (
(1, 4),
(1, 7),
(5, 7),
(10, 7),
(10, 8),
(10, 9),
(3, 4)
)
"""

n = 3

enemies = (
    (1, 2),
    (2, 3)
)

def checkEnemies(rivals):
    #given a pair of rivals, checks to see if those rivals are
    #seated next to each other
    #returns true if there is a problem
    (a, b) = rivals
    
    problem = False
    #pdb.set_trace()    
    for i in range(1, n-1):
        if table[i] == a:
            if table[i+1] == b:
                problem = True
                #print "issue at %d" % i
                
        if table[i] == b:
            if table[i+1] == a:
                problem = True
                #print "issue at %d" %i
                
        #check edges
        if table[0] == a:
            if table[n-1] == b:
                problem == True
                
        if table[0] == b:
            if table[n-1] == a:
                problem == True

    return problem

def tableOK():
    """ returns true if table is
        free of conflicts
    """
    
    ok = True
    for rivals in enemies:
        if checkEnemies(rivals):
            ok = False
    return ok

table = range(1, n+1)
print table
keepGoing = True
counter = 0
while(keepGoing):
    counter += 1
    if tableOK():
        keepGoing = False
        print "Solution: ", table
    else:
        random.shuffle(table)
        
    if counter > 1000:
        print "No solution found"
        keepGoing = False
