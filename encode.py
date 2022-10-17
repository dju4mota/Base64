
def wordToBinary(word):
    binaryWord = ''
    for letter in word:
        binaryWord += "0" + str(bin(ord(letter))[2:])
    return binaryWord

def eigthBitsToSixBits(binaryWord):
  sixBitsWord = ''
  for position in range(0, len(binaryWord), 6):
    if(len(binaryWord[position:position+6]) == 6):
      sixBitsWord += binaryWord[position:position+6]
      #print(binaryWord[position:position+6])
    else:
      sixBitsWord += binaryWord[position:position+6] + "0" * (6 - len(binaryWord[position:position+6]))
      #print(binaryWord[position:position+6] + "0" * (6 - len(binaryWord[position:position+6])))
  return sixBitsWord

def bitsToBase64(sixBitsWord):
  base64Word = ''
  for position in range(0, len(sixBitsWord), 6):
    decimal = int(sixBitsWord[position:position+6], 2)
    base64Word += decimalToBase64(decimal)
    #print(decimalToBase64(decimal))
  return base64Word

def decimalToBase64(decimal):
  base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
  return base64[decimal]
  