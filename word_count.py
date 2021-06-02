# fig06_02.py
"""Tokenizing a string and counting unique words."""
from io import StringIO
from html.parser import HTMLParser
from nltk.corpus import stopwords
import re
import string
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus.reader import WordListCorpusReader

with open('100west.txt', 'r', errors="ignore", encoding='utf-8') as data:
    text = data.read()
data.close()

#sys.exit()

# encoding the text to ASCII format
text_encode = text.encode(encoding="ascii", errors="ignore")
# decoding the text
text_decode = text_encode.decode()
# cleaning the text to remove extra whitespace 
clean_text = " ".join([word for word in text_decode.split()])

#remove URLs
text = re.sub("https?:\/\/.*[\r\n]*", "", text)

#remove uppercase uniqueness
text = text.lower()

#remove punctuation
punct = set(string.punctuation) 
text = "".join([ch for ch in text if ch not in punct])

#remove numbers
text = re.sub("[0-9]", "", text)

# remove common words that add no meaning
stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'many', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", 'yet', 'x']

#Remove stop words and Lematize words
lemmatizer = WordNetLemmatizer()
# Lemmatisation in linguistics is the process of grouping together the inflected forms of a word so they can be analyzed as a single item, identified by the word’s lemma, or dictionary form.
text = " ".join([lemmatizer.lemmatize(word) for word in text.split() if word not in stop_words])

word_counts = {}  # set up word count dictionary

# count occurrences of each unique word
for word in text.split():
    if word in word_counts: 
        word_counts[word] += 1  # update existing key-value pair
    else:
        word_counts[word] = 1  # insert new key-value pair

print(f'{"WORD":<15}COUNT')

# Show word counts occurring when greater than 2
for word, count in sorted(word_counts.items()):
    if count > 2:
        print(f'{word:<15}{count}')

print('\nNumber of unique words:', len(word_counts))
