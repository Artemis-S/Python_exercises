import tweepy
import json
from nltk.tokenize import word_tokenize
import re
from nltk.corpus import stopwords
from collections import Counter
import string

#edo bazo tous ari8mous poy mou edose to twitter otan eftiaksa to app
consumer_key = " "
consumer_secret = " "
access_token = " "
access_token_secret = " "

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#stop words
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']

#anagnorisi emoticons...
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)

def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

def process_or_store(tweet):
    s =json.dumps(tweet)



t = [] #pinakas pou 8a mpoun ola ta tweets

name = raw_input("Please enter your twitter username: ")
print "Hello", name
print "Your last 10 tweets are:"

tweetCount = 10
results = api.user_timeline(id=name, count=tweetCount)
for tweet in results:
    print tweet.text
    j = (tweet._json)  # metatrepo ta tweets se json
    t.append(j)

s =json.dumps(t)
with open("C://Users//Artemis//Desktop//codes//askisi5//tweet.txt", "w") as f:   #ta apo8ikeuo
    f.write(s)

# anigo ton fakelo json kai brisko tin leksi
fname = 'C://Users//Artemis//Desktop//codes//askisi5//tweet.txt'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
        terms_all = [term for term in preprocess(j['text'])]
        # Update the counter
        count_all.update(terms_all)
    print"The most popular word is: ", (count_all.most_common(1))
