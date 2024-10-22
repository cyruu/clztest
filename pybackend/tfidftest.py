import pandas as pd
import math

a = pd.read_csv("reviews.csv")
print(a)

sentences = [
    "i love food",
    "great service",
    "i hate ambiance",
    "the food was amazing",
    "i dislike the noise",
    "fantastic experience",
    "not a good time",
    "the staff was friendly",
    "hate terrible meal",
    "everything was perfect"
]
label = [1,1,0,1,0,1,0,1,0,1]
# vocabulary 
vocabulary = set()
for sentence in sentences:
    tokenizedSentence = sentence.split()
    for token in tokenizedSentence:
        vocabulary.add(token)

vocabulary = sorted(vocabulary)
# tf matrix is 2D array
# TF(t,d) = totalTokenApperedInDoc / totolTokenInDoc
def createTfMatrix(sentences):
    finalTfMatirx = []

    # each sentence (doc)
    for sentence in sentences:
        eachRowTfMatrix = []
        tokenAppearedInDocCount = {}
        tokenizedSentence = sentence.split()
        # create count dictionary for each sentence
        for token in tokenizedSentence:
            totalTokenApperedInDoc = tokenizedSentence.count(token)
            if (token in tokenAppearedInDocCount):
                continue
            tokenAppearedInDocCount[token] = totalTokenApperedInDoc
        # calculate each tf matrix
        # iterate all token in vocabulary list
        for token in vocabulary:
            # check if token in dictionary count in that doc
            if(token in tokenAppearedInDocCount):

                tfOfTokenInDoc = tokenAppearedInDocCount[token] / len(tokenizedSentence)
                eachRowTfMatrix.append(tfOfTokenInDoc)
            else:
                eachRowTfMatrix.append(0)
            
        finalTfMatirx.append(eachRowTfMatrix)
    return finalTfMatirx

finalTfMatrix = createTfMatrix(sentences)

finalTfMatrix = pd.DataFrame(finalTfMatrix,columns=vocabulary)
print("Term Frequency Matrix: TF(t,d)")
print(finalTfMatrix)

# create a IDF matrix
def createIdfMatrix(sentences):
    finalIdfMatrix = []
    totalNoOfDoc = len(sentences)
    totalDocContainingTokenCount = {}
    # initial doc with that token count to 0
    for token in vocabulary:
        totalDocContainingTokenCount[token] = 0
    
    # check for all token in vocab
    # iterate through all token in vocab
    for token in vocabulary:
        # check for every sentence
        for sentence in sentences:
            tokenizedSentence = sentence.split()
            # if token in sentence add one to dict for that token
            if token in tokenizedSentence:
                totalDocContainingTokenCount[token] += 1

    # calulate idf for all token in vocab
    eachIdfValue = []
    for token in vocabulary:
        tokenIdfValue = math.log10(totalNoOfDoc / totalDocContainingTokenCount[token])
        eachIdfValue.append(tokenIdfValue)
    
    finalIdfMatrix.append(eachIdfValue)

    return finalIdfMatrix
       

finalIdfMatrix = createIdfMatrix(sentences)
finalIdfMatrix = pd.DataFrame(finalIdfMatrix,columns=vocabulary)
print("IDF matrix")
print(finalIdfMatrix)
    
def calculateTfIdfMatrix(sentences):
    finalIfIdfMatirx = []
    for i in range(len(sentences)):
        eachTfIdfMatrix = []
        for token in vocabulary:
            tfIdfValue = finalTfMatrix[token][i] * finalIdfMatrix[token][0]
            # print(token, "=>", finalTfMatrix[token][i] ,"*", finalIdfMatrix[token][0] , "=",tfIdfValue)
            eachTfIdfMatrix.append(tfIdfValue)
        finalIfIdfMatirx.append(eachTfIdfMatrix)
    return finalIfIdfMatirx


finalTfIdfMartix = calculateTfIdfMatrix(sentences)
finalTfIdfMartix = pd.DataFrame(finalTfIdfMartix,columns=vocabulary)
print("TF-IDF matrix")
print(finalTfIdfMartix)

# naive bayes
totalSentences = len(label)
totalPositiveSentence = label.count(1)
totalNegativeSentece = label.count(0)

# prior probability for Positive
priorPositiveProbability = totalPositiveSentence/totalSentences
# prior probability for Negative
priorNegativeProbability = totalNegativeSentece/totalSentences
print("prior pos: ",priorPositiveProbability)
print("prior neg: ", priorNegativeProbability)

# likelihood
def calculateLikelihood(sentenceTokenized,classLabel):
    finalLikelihood = 1
    # for unseen words
    # likelihood =  1/total count of tokens in class C
    totalTokenInGivenClass = 0

    for i in range(len(label)):
        if(label[i]==classLabel):
            for token in vocabulary:
                totalTokenInGivenClass += finalTfIdfMartix[token][i]
    print(totalTokenInGivenClass)
    for token in sentenceTokenized:
        likelihoodOfGivenClass = 0
        totalTokenPosOnGivenClass = 0

        # check if token is the feature of the voacb in dataset
        if(token in vocabulary):
            totalNoOfToken = sum(finalTfIdfMartix[token])

            for i in range (len(label)):
                if(finalTfIdfMartix[token][i] > 0 and label[i]==classLabel):
                    totalTokenPosOnGivenClass += finalTfIdfMartix[token][i]
            # if the token not in given class in all dataset
            # zero probability problem
            if(totalTokenPosOnGivenClass == 0):
                likelihoodOfGivenClass = 1 / (totalNoOfToken + len(vocabulary))
            else:
                likelihoodOfGivenClass = totalTokenPosOnGivenClass / totalNoOfToken
        # if the token not in dataset features
        # new word not known to daset (zero prob problem) 
        # likelihood =  1/total count of tokens in class C + len(vocab)
        else:
            likelihoodOfGivenClass = 1 / (totalTokenInGivenClass + len(vocabulary))

        finalLikelihood *= likelihoodOfGivenClass

    return finalLikelihood

sentence = "love"
sentenceTokenized = sentence.split()
likelihoodPositive = calculateLikelihood(sentenceTokenized,1)
likelihoodNegative = calculateLikelihood(sentenceTokenized,0)
print("likelihood poss: ",likelihoodPositive)
print("likelihood negg: ",likelihoodNegative)

posteriorPositiveProbablility = priorPositiveProbability * likelihoodPositive 
posteriorNegativeProbablility = priorNegativeProbability * likelihoodNegative 
print("posteriorPositiveProbablility : ", posteriorPositiveProbablility )
print("posteriorNegativeProbablility  ",posteriorNegativeProbablility )

def calculateSentiment():
    threshold = 0.05
    if(abs(posteriorPositiveProbablility - posteriorNegativeProbablility) <= threshold):
        print("Neutral")

    else:
        if posteriorPositiveProbablility > posteriorNegativeProbablility:
            print("Positive")
        elif posteriorNegativeProbablility > posteriorPositiveProbablility:
            print("Negative")
        

calculateSentiment()








