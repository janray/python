

# Python implementation of Vigenere's Cipher
# by Jan Ray C. Rulida
# November 11, 2014


''' Formula to calculate for the numerical index of an alphanumeric character:

    Index  --> Alphabet
      0    --> A, a
      1    --> B, b
      .
      .
      .
      25   --> Z, z
      
    #---This is for uppercase letters---#
    index = 25 - (90 - asciiValueOfChar) % 26

    #---This is for lowercase letters---#
    index = 25 - (122 - asciiValueOfChar) % 26

'''
while True:
    keyString = raw_input("Please enter keyword. Only alphanumeric characters are allowd: ");
    if keyString.isalpha():
        break


inputString = raw_input("Please enter text to encipher using Vigenere's CIpher: ");

keyLength = len(keyString)

alphaIndexNumber = 0;

keywordIndex = 0

for i in range(len(inputString)):
    if inputString[i].isalpha():
        if inputString[i].isupper():
            alphaIndexNumber = (25 - (90 - ord(keyString[keywordIndex % keyLength].upper())) % 26)
            ciphered = (25 - (90 - ord(inputString[i])) + alphaIndexNumber) % 26

            print chr(65 + ciphered),
        else:
            alphaIndexNumber = (25 - (122 - ord(keyString[keywordIndex % keyLength].lower())) % 26)
            ciphered = (25 - (122 - ord(inputString[i])) + alphaIndexNumber) % 26

            print chr(97 + ciphered),
        keywordIndex += 1
        
    else:
        print inputString[i],

    
        
