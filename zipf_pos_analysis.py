# Kaleb Anderson 
# 301562090
# kga56@sfu.ca
# Project: zipfs-law-pos-brown-corpus
import nltk
nltk.download('brown')
from nltk.corpus import brown
from nltk import FreqDist
# load tagged words with universal tagset
tagged_words = brown.tagged_words(tagset='universal')
# map the categories to the universal tagset
function_tags = {'DET', 'ADP', 'PRON', 'CONJ', 'ADV', 'PRT'}

category_map = {
    'NOUN': 'noun',
    'VERB': 'verb',
    'ADJ': 'adjective'
}
for tag in function_tags:
    category_map[tag] = 'function'

# put brown words into word_categories
words_categorized = [] 

for word, tag in tagged_words:
    category = category_map.get(tag)
    if category:
        words_categorized.append((word, category))

#print(words_categorized[:20])
#print(len(words_categorized))

#clean the words by making them lowercase and remove not words
words_cleaned = []

for word, category in words_categorized:
    word = word.lower()
    if word.isalpha():
        words_cleaned.append((word, category))
print(len(words_categorized))
print(len(words_cleaned))

# checking frequency 
freq = FreqDist(word for word, category in words_cleaned)
print(freq.most_common(20))


# dictionary that stores each unique word with its category, frequency and word legnth together

word_data = {}

for word, category in words_cleaned:
    if freq[word] >= 5:  #  min frequency filter
        if word not in word_data:
            word_data[word] = {
                'category': category,
                'frequency': freq[word],
                'length': len(word)
            }
for word in list(word_data.keys())[:5]:
    print(word, word_data[word])