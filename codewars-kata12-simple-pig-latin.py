#Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

#Examples
#pig_it('Pig latin is cool') # igPay atinlay siay oolcay
#pig_it('Hello world !')     # elloHay orldway !

punctation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

def pig_it(s):
    result = []

    split = s.split()

    for item in split:
        if item not in punctation:
            item = item[1:] + item[0] + 'ay'
            result.append(item)
        elif item in punctation:
            result.append(item)
    return ' '.join(result)
