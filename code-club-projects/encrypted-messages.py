#https://codeclubprojects.org/en-GB/python/secret-messages/

alphabet = 'abcdefghijklmnopqrstuvwxyz'

key = int(input('Please enter your desired key as an integer: '))
               
message = input('Please enter a message: ')

#Create variable to store encrypted message
newMessage = ''

#Write for loop to encrypt message
for character in message:
#Only encrypt if character is in the alphabet
    if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + key) % 26
        newCharacter = alphabet[newPosition]
        newMessage += newCharacter
#Otherwise. just use the original character       
    else:
        newMessage += character

print('Your encrypted message is: ', newMessage)

