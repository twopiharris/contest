""" squads.py
    read in an array of points
    and determine which points are within 50 units of each other
"""

import math

def distance(first, second):
  """given indices of two values
     determine distance between them
  """
  x1 = first[0]
  y1 = first[1]
  x2 = second[0]
  y2 = second[1]
  
  dist = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
  return dist

f = open("squads.txt")
count = f.readline()
count = int(count)
position = []
for i in range(count):
  line = f.readline()
  line = line.strip()
  
  pos = line.split(" ")
  for key, val in enumerate(pos):
    pos[key] = int(val)
  position.append(pos)

count = 0
for i in range(len(position)):
  for j in range(len(position)):
    dist = distance(position[i], position[j])
    if dist < 50:
      if dist > 0:
        print "From %d to %d: %d" % (i, j, dist)
        count += 1

count = count / 2

print "pairs within 50 miles: %d" % count

  
    
  
  
  


