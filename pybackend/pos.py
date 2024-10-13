

import json
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
nlp = spacy.load("en_core_web_sm")

#import getSingular function
from getSingular import getSingular
# load lemma dictionary file
with open('lemmas.txt', 'r',encoding="utf-8") as f:
    wordLemmaDictionary = json.load(f)

#load plural to singular dictionary
with open('plurals.txt', 'r',encoding="utf-8") as f:
    pluralsDictionary = json.load(f)


def lemmatize(token,partOfSpeech):
    if token.text in wordLemmaDictionary and partOfSpeech in wordLemmaDictionary[token.text]:
        return wordLemmaDictionary[token.text][partOfSpeech]
    else:
        return token.text


sentences = ["I am reading a complex buses","This is buying ongoing product","Sam is going abroad this saturday in an flying emergency flights"]


def preprocessSentences(sentences):
    lemmatizedWordsArray = []
    lemmatizedSentences = []
    for sentence in sentences:

        sentence = sentence.lower()
        words = sentence.split()
        words = [word for word in words if word not in STOP_WORDS]

        tempwords = []
        for word in words:
            response = getSingular(word)
            if isinstance(response,dict) and "NOUN" in response:
                tempwords.append(response["NOUN"])
            else:
                tempwords.append(response)

        words = tempwords
        sentence = ' '.join(words)



        doc = nlp(sentence)
   
        lemmatizedWordsArray = []
        for token in doc:
            partOfSpeech = token.pos_
            
            lemma = lemmatize(token,partOfSpeech)
            lemmatizedWordsArray.append(lemma)

        # lemmatizedWordsArray
        # ['read', 'complex', 'bus']
        # ['buy', 'ongoing', 'product']
        # ['sam', 'go', 'abroad', 'saturday', 'fly', 'emergency', 'flight']
        
        lemmatizedSentence = ' '.join(lemmatizedWordsArray)
        lemmatizedSentences.append(lemmatizedSentence)
    # outside loop
    return lemmatizedSentences
        
print("Before lemmatizing")
print(sentences)
sentences = preprocessSentences(sentences)
print("After lemmatizing")
print(sentences)