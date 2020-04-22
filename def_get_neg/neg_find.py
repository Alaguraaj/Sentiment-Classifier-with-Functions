with open("project_twitter_data.csv")as twitter:
    z =twitter.read()
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
def get_neg(z):
    print(z)
    neg_words=string_punctuation(z)
    print(neg_words)
    neg_count=0
    for i in neg_words.split():
        if i in negative_words:
            neg_count+=1      
    return neg_count
            
def string_punctuation(words):
    for i in punctuation_chars:
        if i in words:
            words=words.replace(i,'')
    return words

check=get_neg("The weather truely is abnormal - it's october and already snowing!")
print(check)
