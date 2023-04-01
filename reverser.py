""" reverser.py """

data = (
  (24, 1),
  (4358, 754),
  (305, 794)
)

def reverse(num):
    numStr = str(num)
    newStr = numStr[::-1]
    revNum = int(newStr)
    return revNum
    
for pair in data:
    (a, b) = pair
    revA = reverse(a)
    revB = reverse(b)
    sum = revA + revB
    print reverse(sum)
    