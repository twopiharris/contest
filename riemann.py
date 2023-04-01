""" riemann sum """

dx = .001
line = "0 1 1 7"
#line = "3 1 3 3 7 -4 4"

vals = line.split(" ")

#convert vals to integers
for key, item in enumerate(vals):
  vals[key] = float(item)
  
#separate coefficients from bounds
coef = vals[:-2]
lBound = vals[-2]
uBound = vals[-1]


print vals
print "coef:", coef
print "lBound:", lBound
print "uBound", uBound

sum = 0
x = lBound
while x < uBound:
  for power, co in enumerate(coef):
    sum += (co * (x**power))*dx
    print "sum:", sum
  
  x += dx
  
  
print sum
  