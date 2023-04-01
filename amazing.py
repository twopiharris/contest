#!/usr/bin/env python
""" Amazing.py
    find an amazing number
    2519 mod 1 = 0
             2 = 1
             ...
             10 = 9
"""

max = input("max value: ")
for n in range(max + 1):
  if n % 1 == 0:
    if n % 2 == 1:
      if n % 3 == 2:
        if n % 4 == 3:
          if n % 5 == 4:
            if n % 6 == 5:
              if n % 7 == 6:
                if n % 8 == 7:
                  if n % 9 == 8:
                    if n % 10 == 9:
                      print n

