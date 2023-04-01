""" bizBaz.py
Biz: 2
Baz: 3
Buzz: 5
Boz: 7
Beez: 11
Bizzle: 13
"""

inFile = open("bizbazIn.txt", "r")
outFile = open("bizBazOut.txt", "w")

primes = (2,     3,     5,      7,    11,     13)
terms = ("Biz ", "Baz ", "Buzz ", "Boz ", "Beez ", "Bizzle ")

for line in inFile:
    freq = int(line)
    hit = True
    outFile.write(str(freq))
    outFile.write(" ")
    for i in range(len(primes)):
        prime = primes[i]
        #print freq, prime, 
        if freq % prime == 0:
            hit = False
            outFile.write(terms[i]) 
    if hit:
        outFile.write("Bummer")
    outFile.write("\n");

inFile.close()
outFile.close()

