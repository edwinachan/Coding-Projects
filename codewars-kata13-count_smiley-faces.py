#Description:
#Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

#Rules for a smiling face:
#-Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
#-A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
#-Every smiling face must have a smiling mouth that should be marked with either ) or D.
#No additional characters are allowed except for those mentioned.
#Valid smiley face examples:
#:) :D ;-D :~)
#Invalid smiley faces:
#;( :> :} :] 

#countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
#countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
#countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;

validEyes = ':;'

validNose = '~-'

validMouth = ')D'

def count_smileys(arr):

    count = 0

    for item in arr:
        if item[0] in validEyes and item[1] in validMouth:
            count +=1
        if item[0] in validEyes and item[1] in validNose and item[2] in validMouth:
            count +=1
    return count
