#List of punctuation
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
#List of Positive words
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
#List of Negative words
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
#function to find out the positive words in the twitter data
def get_pos(words):
    #print(words)
    pos_words=strip_punctuation(words)
    #call the strip function
    pos_count=0
    #print(pos_words)
    #print('Check for Positive Strings--------{}'.format(pos_words))
    for i in pos_words.lower().split():
        #print(i)
        if i in positive_words:
            pos_count+=1
    return pos_count
#function to find out the Negative words in the twitter data               
def get_neg(words):
    #print(words)
    neg_words=strip_punctuation(words)
    #print(neg_words)
    neg_count=0
    for i in neg_words.lower().split():
       # print(i)
        if i in negative_words:
            neg_count+=1 
            #print(i)
    return neg_count
#Sub_function to remove the punctuation characters            
def strip_punctuation(word):
    
    for i in punctuation_chars:
        if i in word:
            word=word.replace(i,'')
    return word

# output the header row
sentiment_classifier = open("resulting_data.csv", "w")
sentiment_classifier.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
sentiment_classifier.write('\n')

#opening and reading the fake generated twitter data 
with open('project_twitter_data.csv','r') as twitter:
    words=twitter.readlines()

header_lines = words[0]
print(header_lines)
header_name = header_lines.strip().split(',')
print(header_name)

for lin in words[1:]:
    
    fun = lin.strip().split(',')
    lin_string = '{},{},{},{},{}'.format(fun[1],fun[2],get_pos(fun[0]),get_neg(fun[0]),get_pos(fun[0])-get_neg(fun[0]))
    sentiment_classifier.write(lin_string)
    sentiment_classifier.write('\n')

sentiment_classifier.close()

