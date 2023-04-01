""" t9.py
    Given a phone number containing only digits 2-9,
    print out all the letter combinations that can be
    formed with this number (Not just English words -
    all possibilities)
"""

import pdb

keys = {
    2: ("A", "B", "C"),
    3: ("D", "E", "F"),
    4: ("G", "H", "I"),
    5: ("J", "K", "L"),
    6: ("M", "N", "O"),
    7: ("P", "Q", "R", "S"),
    8: ("T", "U", "V"),
    9: ("W", "X", "Y", "Z")
}

def addLetters(currentString, keyNum):
    """ given a current string and a key number,
        generates an array of words based on the
        currentString adding each of the characters
        indicated by the keyNum
    """
    
    outList = []
    letters = keys[keyNum]
    for letter in letters:
        outList.append(currentString + letter)
        
    return outList

number = 328
numString = str(number)

word = ""
wordList = [""]
for keyPos in range(len(numString)):
    newList = []
    for word in wordList:
        #print word
        newList += addLetters(word, int(numString[keyPos]))
        
    wordList = newList

final = [x for x in wordList if len(x) == len(numString)]

for word in final:
    print word
