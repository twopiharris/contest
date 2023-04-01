""" bigFib.py """

def calcFibOld(limit):
    a = 1
    b = 1
    finNum = 0
    while finNum < limit:
       newNum = a + b
       a = b
       b = newNum
       finNum = sum(map(int,str(newNum)))
    return finNum

def calcFib(limit):
    a = 1
    b = 1
    sum = 0
    #print 1,1,
    for i in range(limit-2):
        sum = a + b
        a = b
        b = sum
        
        #print sum,
        
    #print
    return(sum)

def main():
    inFile = open("bigFibIn.txt", "r")
    for line in inFile:
        limit = int(line)
        print calcFib(limit)
        
    inFile.close()
    
if __name__ == "__main__":
    main()
    #print calcFib(5)


