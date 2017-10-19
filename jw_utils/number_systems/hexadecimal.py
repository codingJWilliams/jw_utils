# Jay Williams 2017
# This module is included as part of https://github.com/codingJWilliams/jw_utils
# Liscenced according to ../../LISCENCE
# Contact codingJWilliams on github with any queries

def to_decimal(hex):
  hexArray = list(reversed([x for x in hex ]))
  finalNumber = 0
  digitMapping = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
  }
  for i, digit in enumerate(hexArray):
    finalNumber += ( digitMapping[digit] * (16 ** ( i )) )
  return finalNumber
def to_format(dec):
  hexArray = []
  rt = dec
  i = 0
  while (16**i) <= dec:
    i += 1
  
  print(i)