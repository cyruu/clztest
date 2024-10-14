

import json
import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

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


sentences = ["I am reading a complex buses","This is buying ongoing product","Sam is going abroad this saturday and reading in a flying emergency flights"]
sentences = [
    "I am reading a complex book",               # 0
    "She is planning a trip to the mountains",   # 0
    "He is buying a new laptop today",           # 1
    "They are enjoying the sunny weather",       # 0
    "I need to purchase some groceries",         # 1
    "This is the best product in the market",    # 1
    "We are hiking in the hills this weekend",   # 0
    "He is booking a flight for his vacation",   # 0
    "The store is offering a huge discount",     # 1
    "She is making a big investment in stocks",  # 1
    "He loves reading about different cultures", # 0
    "The company is launching a new product",    # 1
    "I will be traveling abroad next month",     # 0
    "He is negotiating a deal with investors",   # 1
    "We are planning a family gathering",        # 0
    "I need to return the faulty product",       # 1
    "Sam is reading a mystery novel",            # 0
    "The team is working on a new business plan",# 1
    "He is visiting his grandparents this weekend", # 0
    "The customer is requesting a refund"        # 1
]

labels = [
    0, 0, 1, 0, 1, 1, 0, 0, 1, 
    1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1
]


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
        

sentences = preprocessSentences(sentences)

vectorizer = CountVectorizer()

# Fit and transform the lemmatized sentences into a bag of words
bag_of_words = vectorizer.fit_transform(sentences)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(bag_of_words, labels, test_size=0.2, random_state=42)
# Initialize the Naive Bayes classifier
nb_classifier = MultinomialNB()

# Train the classifier on the training data
nb_classifier.fit(X_train, y_train)
# Predict on the test data
y_pred = nb_classifier.predict(X_test)

# Calculate accuracy (for evaluation purposes)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

new_sentences = [
    "I am buying a new phone",        # Likely negative (1)
    "She is reading a book outside",  # Likely positive (0)
]

# Preprocess and vectorize the new sentences
new_sentences = preprocessSentences(new_sentences)
new_bag_of_words = vectorizer.transform(new_sentences)

# Predict the labels for new data
new_predictions = nb_classifier.predict(new_bag_of_words)

# Output predictions for new data
for sentence, pred in zip(new_sentences, new_predictions):
    sentiment = "positive" if pred == 0 else "negative"
    print(f"Sentence: '{sentence}' is predicted as {sentiment}")