from math import frexp

def convertFloat2Fixed(n, q1, q2):
  
  if (n < 0):
    negFlag = 1
  else:
    negFlag = 0

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

  if (negFlag):
    bMantissa, bOrdinate = twosComplement(bMantissa, bOrdinate, q1, q2)
    print("The 2's complement is: ", bMantissa, bOrdinate)

def twosComplement(bMantissa, bOrdinate, q1, q2):
  bString = list(bMantissa + bOrdinate)

  #First, find 1's complement.
  for i in range(len(bString) - 1, -1, -1):
    if (bString[i] == '0'):
      bString[i] = '1'
    elif (bString[i] == '1'):
      bString[i] = '0'

  #Now, 2's complement.
  carry = '1'
  for i in range(len(bString) - 1, -1, -1):
    if carry == '0':
      break

    elif bString[i] == '0':
      bString[i] = carry
      carry = '0'
    
    elif bString[i] == '1':
      bString[i] = '0'

  return ''.join(bString[0:q1]), ''.join(bString[q1:])
