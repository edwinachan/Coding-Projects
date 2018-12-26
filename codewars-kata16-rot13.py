#According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.

#Hint: For this task you're only supposed to substitue characters. Not spaces, punctuation, numbers etc. Test examples:

#rot13("EBG13 rknzcyr.") == "ROT13 example.";
#rot13("This is my first ROT13 excercise!" == "Guvf vf zl svefg EBG13 rkprepvfr!"

def rot13(message):
    newMessage = ''
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                newLetter = letter.lower()
                newLetter = alphabet.index(newLetter) + 13
                if newLetter >= 26:
                    newMessage += alphabet[newLetter % 26].upper()
                else:
                    newMessage += alphabet[newLetter].upper()
            else:
                newLetter = alphabet.index(letter) + 13
                
                if newLetter >= 26:
                    newMessage += alphabet[newLetter % 26]
                else:
                    newMessage += alphabet[newLetter]
        else:
            newMessage += letter
    return newMessage
