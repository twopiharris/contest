""" radioRange.py """
import math

data = (
    (0, 0, 5, 9, 0, 5),
    (0, 0, 5, 11, 0, 5),
    (0, 0, 5, 10, 0, 5))

for line in data:

    (x1, y1, r1, x2, y2, r2) = line
    dist = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    #print dist,
    if (r1 + r2) < dist:
        print "OUT OF RANGE"
    elif (r1 + r2) > dist:
        print "IN RANGE"
    else:
        print "MAX RANGE"