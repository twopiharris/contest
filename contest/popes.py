"""
popes.py

INPUT (range, numPopes, each line year of election)
5
20
1
2
3
6
8
12
13
15
16
17
18
19
20
20
21
25
26
30
31

OUTPUT (max num popes in range, year begin, year end)
6 16 20

"""
inFile = open("popesInput.txt", "r")

rawData = []
for line in inFile:
    rawData.append(int(line))

inFile.close()

print rawData
print rawData[0]

yearSpan = rawData[0]
numPopes = rawData[1]
popeYears = rawData[2:]

totalSpan = popeYears[-1] - popeYears[0]



print "yearSpan: %d" % yearSpan
print "numPopes: %d" % numPopes
print "total span:", totalSpan

print popeYears

popeID = 0
currentPope = popeYears[popeID]
nextPope = popeYears[popeID + 1]
for year in range(1, totalSpan +2):
    if year >= nextPope:
        popeID += 1
        currentPope = popeYears[popeID]
        if popeID <= yearSpan -1:
            nextPope = popeYears[popeID + 1]
        else:
            nextPope = 9999
    print year, currentPope
   

