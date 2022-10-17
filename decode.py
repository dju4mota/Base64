
def binaryToWord(binaryWord):
  word = ''
  for position in range(0, len(binaryWord), 8):
    word += chr(int(binaryWord[position:position+8], 2))
  return word

def sixBitsToEightBits(sixBitsWord):
  eightBitsWord = ''
  for position in range(0, len(sixBitsWord), 8):
      eightBitsWord += sixBitsWord[position:position+8]
  return eightBitsWord

def base64ToBits(base64Word):
  sixBitsWord = ''
  for letter in base64Word:
    decimal = base64ToDecimal(letter)
    sixBitsWord += "0" * (6 - len(bin(decimal)[2:])) + bin(decimal)[2:]
  return sixBitsWord

def base64ToDecimal(base64):
  decimal = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
  return decimal.index(base64)