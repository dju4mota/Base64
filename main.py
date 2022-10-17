from encode import wordToBinary, eigthBitsToSixBits, bitsToBase64
from decode import binaryToWord, sixBitsToEightBits, base64ToBits

#word to base64
def encodeWord(wordToEncode):
  binaryWord = wordToBinary(wordToEncode)
  sixBitsWord = eigthBitsToSixBits(binaryWord)
  base64Word = bitsToBase64(sixBitsWord)
  return base64Word

def decodeWord(wordToDecode):
  sixBitsWord = base64ToBits(wordToDecode)
  eightBitsWord = sixBitsToEightBits(sixBitsWord)
  word = binaryToWord(eightBitsWord)
  return word
  

wordToEncode = input("Enter a word to encode: ")
print(encodeWord(wordToEncode))

print(decodeWord(encodeWord(wordToEncode)))