
import pandas as pd
import re
from nltk.corpus import wordnet 
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import nltk
import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

from flask import Flask,request,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/getflaskdata", methods=["POST"])
def getflaskdata():
    
    data = request.json
    nlp = spacy.load("en_core_web_sm")

    words = "eat eats eating showing ability disappointing misleading" 

    # vectorizer = CountVectorizer()
    vectorizer = TfidfVectorizer()
    lemmatizer = WordNetLemmatizer()

    stopwords = [
        "i", "me", "my", "myself", "we", "our", "ours", "ourselves",
        "you", "your", "yours", "yourself", "yourselves", "he", "him",
        "his", "himself", "she", "her", "hers", "herself", "it", "its",
        "itself", "they", "them", "their", "theirs", "themselves", "what",
        "which", "who", "whom", "this", "that", "these", "those", "am",
        "is", "are", "was", "were", "be", "been", "being", "have", "has",
        "had", "having", "do", "does", "did", "doing", "a", "an", "the",
        "and", "but", "if", "or", "because", "as", "until", "while", "of",
        "at", "by", "for", "with", "about", "against", "between", "into",
        "through", "during", "before", "after", "above", "below", "to",
        "from", "up", "down", "in", "out", "on", "off", "over", "under",
        "again", "further", "then", "once", "here", "there", "when",
        "where", "why", "how", "all", "any", "both", "each", "few",
        "more", "most", "other", "some", "such", "no", "nor", "not",
        "only", "own", "same", "so", "than", "too", "very", "s", "t",
        "can", "will", "just", "don", "should", "now"
    ]


    df = pd.read_csv("./reviews.csv")
    reviews = df["review"]
    output = df["output"]

    # lowercase
    reviews = reviews.str.lower()

    # cleaned_reviews = [re.sub(r'[^a-z\s]', '', review.lower()) for review in reviews]
    # remove puncuations, digits , special characters
    reviews = [re.sub(r'[^a-z\s]','',review) for review in reviews]
    # cleaned_review = re.sub(r'\s+', ' ', cleaned_review)
    # remove all white space with one white space
    reviews = [re.sub(r'\s+',' ',review) for review in reviews]
    # ['i dont like this product', 'i absolutely love this product it works wonders']

    tempreviews = []
    for review in reviews:
        #review in this form
        # will definitely buy again super satisfied
        # this product is a scam
        

        # split into each word
        eachwords = review.split()
        # ['very', 'unhappy', 'with', 'the', 'results']
        # print(eachwords)

        eachwords = [word for word in eachwords if word not in stopwords]
        # print(eachwords)
        # ['unhappy', 'results']
        doc = nlp(" ".join(eachwords))
        # print(doc)
        # total waste money disappointed
        tempreview = []
        for word in doc:
            tempreview.append(word.lemma_)
        # print(tempreview)
        # ['total', 'waste', 'money', 'disappoint']
        review = single_string = ' '.join(tempreview)
        # print(review)
        # total waste money disappoint

        # array of reviews after lemmatizing
        tempreviews.append(review)
        

        # print("-------------------------------------")

    reviews = tempreviews
    labels = df['output']

    X = vectorizer.fit_transform(reviews)

    X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

    nb_classifier = MultinomialNB()

    # Train the classifier on the training data
    nb_classifier.fit(X_train, y_train)

    #### 3. Make Predictions and Evaluate the Classifier


    # Make predictions on the test set
    y_pred = nb_classifier.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)


    def predict_review_sentiment(review_text):
        # Transform the new review using the same TF-IDF vectorizer
        review_tfidf = vectorizer.transform([review_text])
        
        # Predict the label (0 for negative, 1 for positive)
        prediction = nb_classifier.predict(review_tfidf)
        
        # Convert the numeric prediction to a human-readable result
        if prediction[0] == 1:
            return "Positive"
        else:
            return "Negative"

    # Example: Predicting the sentiment of a new review
    new_review = data["bodyData"]
    result = predict_review_sentiment(new_review)
    print(f'The sentiment of the review is: {result}')








    #Lemmatization 
    # nlp should be a string not array

    # for token in doc:
    #     print(token," | ", token.lemma_)



    # print(lemmatized_tokens)



    return jsonify({"sentiment":data["bodyData"]})

if __name__ == "__main__":
    print("running in porrt 8000")
    app.run(debug=True, port=8000)

