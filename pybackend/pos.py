

import json
import spacy

nlp = spacy.load("en_core_web_sm")

#import getSingular function
from getSingular import getSingular
# load lemma dictionary file
with open('lemmas.txt', 'r',encoding="utf-8") as f:
    wordLemmaDictionary = json.load(f)

#load plural to singular dictionary
with open('plurals.txt', 'r',encoding="utf-8") as f:
    pluralsDictionary = json.load(f)


sentence = "I am reading a complex"

doc = nlp(sentence)
for token in doc:
    print(token,"|",token.pos_)

# nned to create a lemmatizer funtion that gives word if in dictionary eelse return as it is. "complex" eg