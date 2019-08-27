from math import frexp

def convertFloat2Fixed(n, q1, q2):
  numberStr = str(n)
  pointIdx = numberStr.find('.')

  #Find mantissa and ordinates
  mantissa = numberStr[0 : pointIdx]
  ordinate = '0.' + numberStr[pointIdx + 1 : ]

  bMantissa = str(bin(int(mantissa)))
  fOrdinate = float(ordinate)

  #Convert the binary mantissa to a width of q1
  #Index of 'b'
  bIdx = bMantissa.find('b')
  bMantissa = bMantissa[bIdx + 1 :]
  
  #For positive numbers, go on including a '0' at the MSB
  while (len(bMantissa) < q1):
    bMantissa = '0' + bMantissa

  #Do the overflow.
  bMantissa = bMantissa[-q1:]
  print(bMantissa)
  #print(fOrdinate)

  #Fix up the binary ordinate
  bOrdinate = ''
  for i in range(0, q2):
    k = 2*fOrdinate
    digit = int(k)
    bOrdinate = bOrdinate + str(digit)
    fOrdinate = k - int(k)

  print(bOrdinate)
