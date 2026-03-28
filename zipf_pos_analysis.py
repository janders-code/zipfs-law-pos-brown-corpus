# Kaleb Anderson 
# 301562090
# kga56@sfu.ca
# Project: zipfs-law-pos-brown-corpus
import nltk
import csv

nltk.download('brown')
from nltk.corpus import brown
from nltk import FreqDist

tagged_words = brown.tagged_words(tagset='universal')

function_tags = {'DET', 'ADP', 'PRON', 'CONJ', 'PRT'}

category_map = {
    'NOUN': 'noun',
    'VERB': 'verb',
    'ADJ': 'adjective'
}
for tag in function_tags:
    category_map[tag] = 'function'

words_categorized = [] 
for word, tag in tagged_words:
    category = category_map.get(tag)
    if category:
        words_categorized.append((word, category))

words_cleaned = []
for word, category in words_categorized:
    word = word.lower()
    if word.isalpha():
        words_cleaned.append((word, category))

freq = FreqDist(word for word, category in words_cleaned)

word_data = {}
for word, category in words_cleaned:
    if freq[word] >= 5:
        if word not in word_data:
            word_data[word] = {
                'category': category,
                'frequency': freq[word],
                'length': len(word)
            }

with open('word_data.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['word', 'category', 'frequency', 'length'])
    writer.writeheader()
    for word, data in word_data.items():
        writer.writerow({
            'word': word,
            'category': data['category'],
            'frequency': data['frequency'],
            'length': data['length']
        })


