punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

#with open("project_twitter_data.csv ","r") as twitter :
#    print (twitter.read())
    
def strip_punctuation(words):
    for i in punctuation_chars:
        words=words.replace(i,'')
    print(words)
    return words
    
check=strip_punctuation('Strip, Test!!!')
print(check)
