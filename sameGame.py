""" sameGame.py

  1 3 5 2 2
  2 2 3 5 1
  1 2 3 5 5
  
"""

import pdb

board = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 1, 3, 5, 2, 2, 0],
  [0, 2, 2, 3, 5, 1, 0],
  [0, 1, 2, 3, 5, 5, 0],
  [0, 0, 0, 0, 0, 0, 0]
]

WIDTH = 5
HEIGHT = 3
pWidth = WIDTH + 2
pHeight = HEIGHT + 2

def collapseCols():
    #collapse any zeros
    for row in range(1, HEIGHT):
        for col in range(1, WIDTH):
            if board[row+1][col] == 0:
                board[row+1][col] = board[row][col]
                board[row][col] = 0                
    
def collapseRows():
    #collapses a col with all zeros
    for col in range(1, WIDTH + 1):

        empty = True
        for row in range(1, HEIGHT+ 1):
            #print "r: %d, c: %d, %d" % (row, col, board[row][col])
            if board[row][col] != 0:
                empty = False
        if empty:
            #print "Column %d is empty" % col
            for row in range(1, HEIGHT +1):
                board[row][col] = board[row][col+1]
                board[row][col+1] = 0
    
def findRegion(row, col):
    #recursive function to mark members of a group
    print ""
    myVal = board[row][col]
    if myVal == 0:
        print "Can't remove this cell"
        print "r: %d, c: %d, %d" % (row, col, board[row][col])

    else:
        board[row][col] = 0
        north = board[row-1][col]
        south = board[row+1][col]
        east = board[row][col-1]
        west = board[row][col+1]
        
        if myVal == north:
            findRegion(row-1, col)
        if myVal == south:
            findRegion(row+1, col)
        if myVal == east:
            findRegion(row, col-1)
        if myVal == west:
            findRegion(row, col+1)

        collapseCols()
        collapseRows()
        
def printBoard():
    for row in range(pHeight):
        for col in range(pWidth):
           print board[row][col],
        print
    print
    
printBoard()
findRegion(2,1)
print "removing (2,1)"
printBoard()
print "removing (3,3)"
findRegion(3, 3)
printBoard()

"""

print "removing (3,2)"
print board[3][3]
findRegion(3,3)
printBoard()

findRegion(3,1)
printBoard()
"""



