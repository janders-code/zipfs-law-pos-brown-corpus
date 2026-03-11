# Trials and Tests

import nltk
nltk.download('brown')
from nltk.corpus import brown

# categories in the corpus
#print(brown.categories())

# See first 20 tagged words
#print(brown.tagged_words()[:20])

#tags = set(tag for word, tag in brown.tagged_words())
#print(sorted(tags))

"""
Nouns: NN, NNS, NP, NPS, NR, NRS
Verbs: VB, VBD, VBG, VBN, VBZ, BE, BED, BEDZ, BEG, BEM
BEN, BER, BEZ, HV, HVD, HVG, HVN, HVZ, DO, DOD, DOZ, M
Adjectives: JJ, JJR, JJS, JJT
Function words: AT, DT, DTI, 


list of stuff to do

Map words to categories (noun, verb, adjective, function)
Filter and categorize all words 
Clean the words 
Count frequency 
Filter by minimum frequency 
Measure word length
Log transform the frequency 
"""

tagged_words = brown.tagged_words(tagset='universal')
print(tagged_words[:20])