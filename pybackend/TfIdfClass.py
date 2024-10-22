import pandas as pd
import math

class TfIdfClass:

    def __init__(self):
        
        self.vocabulary = set()
        self.finalIdfMatrix = []
        self.finalTfMatrix = []
        self.finalIfIdfMatirx = []
    
    # create vocabulary array
    def createVocabulary(self,sentences):

        for sentence in sentences:
            tokenizedSentence = sentence.split()
            for token in tokenizedSentence:
                self.vocabulary.add(token)
        
        return sorted(self.vocabulary)
    
    # create Term Frequency Matrix
    def createTfMatrix(self,sentences):
        
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
            for token in self.vocabulary:
                # check if token in dictionary count in that doc
                if(token in tokenAppearedInDocCount):

                    tfOfTokenInDoc = tokenAppearedInDocCount[token] / len(tokenizedSentence)
                    eachRowTfMatrix.append(tfOfTokenInDoc)
                else:
                    eachRowTfMatrix.append(0)
                
            self.finalTfMatrix.append(eachRowTfMatrix)
        return self.finalTfMatrix

    # create a IDF matrix
    def createIdfMatrix(self,sentences):
        
        totalNoOfDoc = len(sentences)
        totalDocContainingTokenCount = {}
        # initial doc with that token count to 0
        for token in self.vocabulary:
            totalDocContainingTokenCount[token] = 0
        
        # check for all token in vocab
        # iterate through all token in vocab
        for token in self.vocabulary:
            # check for every sentence
            for sentence in sentences:
                tokenizedSentence = sentence.split()
                # if token in sentence add one to dict for that token
                if token in tokenizedSentence:
                    totalDocContainingTokenCount[token] += 1

        # calulate idf for all token in vocab
        eachIdfValue = []
        for token in self.vocabulary:
            tokenIdfValue = math.log10(totalNoOfDoc / totalDocContainingTokenCount[token])
            eachIdfValue.append(tokenIdfValue)
        
        self.finalIdfMatrix.append(eachIdfValue)

        return self.finalIdfMatrix
    
    # create TF-IDF Matrix
    def calculateTfIdfMatrix(self,sentences):
        
        for i in range(len(sentences)):
            eachTfIdfMatrix = []
            for token in self.vocabulary:
                tfIdfValue = self.finalTfMatrix[token][i] * self.finalIdfMatrix[token][0]
                # print(token, "=>", finalTfMatrix[token][i] ,"*", self.finalIdfMatrix[token][0] , "=",tfIdfValue)
                eachTfIdfMatrix.append(tfIdfValue)
            self.finalIfIdfMatirx.append(eachTfIdfMatrix)
        return self.finalIfIdfMatirx
    


tfidf = TfIdfClass()
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
# vocabulary = tfidf.createVocabulary(sentences)
