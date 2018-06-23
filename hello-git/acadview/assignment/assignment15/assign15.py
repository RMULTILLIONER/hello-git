#Q.1- Extract the user id, domain name and suffix from the following email addresses.
#emails = "zuck26@facebook.com""page33@google.com""jeff42@amazon.com"
#desired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')]

import re
emails = " zuck26@facebook.com" "page33@google.com" "jeff42@amazon.com"
pattern = r'(\w+)@([A-Z0-9]+).([A-Z]{3})'
print(re.findall(pattern, emails, re.IGNORECASE))




#Q.2- Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
#text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better." 

text = 'Betty bought a bit of butter, But the butter was so bitter , So she bought some better butter, To make the bitter butter better.'
import re
print(re.findall(r'\bB\w+',text,flags=re.IGNORECASE))




#Q.3- Split the following irregular sentence into words
#sentence = "A, very very; irregular_sentence"
#desired_output = "A very very irregular sentence"

import re
regex_compile = re.compile('[^_\W]+')
l = regex_compile.findall('A, very very; irregular_sentence')
print(l)
l = [(i.split('\t',1)[0]) for i in l]
print(" ".join(l))




#Q.4- Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.
#tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
#desired_output = 'Good advice What I would do differently if I was learning to code today'

tweet="'Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'"
import re
def clean_tweets(tweet):
    #remove URLs
    tweet=re.sub('http\S+\s*',' ',tweet)
    #remove RT and cc
    tweet = re.sub('RT|cc', ' ', tweet)
    #remove hashtags
    tweet = re.sub('#\S+', ' ', tweet)
    #remove mentions
    tweet = re.sub('@\S+', ' ', tweet)
    #remove punctuations
    tweet = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_'{|}~"""), ' ', tweet)
    #remove extra whitespace
    tweet=re.sub('\s+',' ',tweet)
    return tweet

print(clean_tweets(tweet))



