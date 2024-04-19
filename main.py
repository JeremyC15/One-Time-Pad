import random

alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
message = input("Enter message:")

def cleantext(clean):
  
  clean = ''.join(c for c in message if c.isalnum())
  clean = clean.lower()
  clean = ''.join(clean)
  
  return clean

def generatekey(clean):
  key = ''
  for letter in range(len(clean)):
    key = key + random.choice(alpha)
  return key
  
     
def encrypt(message,key):
  encrypt = ''
  for character,letter in zip(message, key):
    joined = ord(character) + ord(letter)
    encrypt = encrypt + chr(joined)
  return encrypt


def decrypt(encryptedtext,key):
  decrypted = ''
  for character,letter in zip(encryptedtext, key):
    joined = ord(character) - ord(letter)
    decrypted = decrypted + chr(joined)
  return decrypted
    
text = cleantext(message)

key = generatekey(text)

print("Key: " + key)

encrypted = encrypt(text,key)

print("Encrypted: " + encrypted)

encryptText = input("Enter encrypted text: ")

keyText = input("Enter key: ")

decrypted = decrypt(encryptText, keyText)

print("Decrypted Message: " + decrypted)