# A Caesar Cipher is a simple cipher that works by shifting each letter in
# the given message by a certain number. For example, if we shift the message
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given
# message by shift letters. You are guaranteed that message is a string, and
# that shift is an integer between -25 and 25. Capital letters should stay capital
# and lowercase letters should stay lowercase, and non-letter characters should not be changed.
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")

# reference from https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/

def fun_applycaesarcipher(msg, shift):
    cipherMsg = ''
    # looping through the msg
    for char in msg:
        # a=97 z=122
        # ord converts string to integer
        # chr converts the integer to a character string
        if char.islower():
            cipherMsg += chr((ord(char)-97+shift) % 26+97)
        # A=65 Z=90
        elif char.isupper():
            cipherMsg += chr((ord(char)-65+shift) % 26+65)
        else:
            cipherMsg += char
    return cipherMsg
