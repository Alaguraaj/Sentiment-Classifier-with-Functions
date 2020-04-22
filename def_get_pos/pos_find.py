punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
print(positive_words)

def get_pos(x):
    print(x)
    pos_words=strip_punctuation(x)
    #call the strip function
    pos_count=0
    #print(pos_words)
    print('Check for Positive Strings--------{}'.format(pos_words))
    for i in pos_words.lower().split():
        print(i)
        if i in positive_words:
            pos_count+=1
    return pos_count
def strip_punctuation(string_word):
    for i in punctuation_chars:
        if i in string_word:
            string_word=string_word.replace(i,'')
    print(string_word)
    return string_word
    
check=get_pos('what a truly Wonderful day it is today! #incredible')
print(check)
