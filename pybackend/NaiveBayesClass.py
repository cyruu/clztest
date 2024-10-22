import pandas as pd
import numpy as np
from TfIdfClass import TfIdfClass
from DataClass import DataClass

class NaiveBayesClass:

    def __init__(self):
        # create TfIdfClass instance
        self.tfidf = TfIdfClass()
        df = pd.read_csv("reviews.csv")
        self.sentences = df["review"].to_numpy()
        self.label = df["label"].to_numpy()
        # for preprocessing DataClass
        self.dc = DataClass()
        # for TF-IDF
        self.vocabulary = set()
        self.finalTfMatrix= []
        self.finalTfIdfMartix = []

        # for Naive Bayes
        self.totalSentences = len(self.label)
        self.totalPositiveSentence = np.count_nonzero(self.label == 1)
        self.totalNegativeSentence = np.count_nonzero(self.label == 0)

    def calculateSentiment(self,sentence):
        # preprocess the sentences
        self.sentences = self.dc.preprocessSentences(self.sentences)
        print(self.sentences[1])
        vocabulary = self.tfidf.createVocabulary(self.sentences)
        finalTfMatrix = self.tfidf.createTfMatrix(self.sentences)
        finalTfMatrix = pd.DataFrame(finalTfMatrix,columns=vocabulary)
        print("Term Frequency Matrix: TF(t,d)")
        # print(finalTfMatrix["not"][1],finalTfMatrix["like"][1],finalTfMatrix["product"][1])
        # print(finalTfMatrix)
        # self.finalTfMatrix = self.tfidf.createTfMatrix(self.sentences)
        # self.vocabulary = self.tfidf.createVocabulary(self.sentences)
        # print(self.vocabulary)
        [priorPositiveProbability,priorNegativeProbability] = self.calculatePriorProbability()
        # split given sentence into tokens
        sentenceTokenized = sentence.split()
        # likelihoodPositive = self.calculateLikelihood(sentenceTokenized,1)
        # likelihoodNegative = self.calculateLikelihood(sentenceTokenized,0)
        # print(priorPositiveProbability,priorNegativeProbability)
        # print(likelihoodPositive,likelihoodNegative)
        
    # prior probability calculation
    def calculatePriorProbability(self):
        # prior probability for Positive
        priorPositiveProbability = self.totalPositiveSentence/self.totalSentences
        # prior probability for Negative
        priorNegativeProbability = self.totalNegativeSentence/self.totalSentences

        return [priorPositiveProbability,priorNegativeProbability]

    # likelihood calculation
    def calculateLikelihood(self,sentenceTokenized,classLabel):
        finalLikelihood = 1
        # for unseen words
        # likelihood =  1/total count of tokens in class C
        totalTokenInGivenClass = 0

        for i in range(self.totalSentences):
            if(self.label[i]==classLabel):
                for token in self.vocabulary:
                    totalTokenInGivenClass += self.finalTfIdfMartix[token][i]
        print(totalTokenInGivenClass)
        for token in sentenceTokenized:
            likelihoodOfGivenClass = 0
            totalTokenPosOnGivenClass = 0

            # check if token is the feature of the voacb in dataset
            if(token in self.vocabulary):
                totalNoOfToken = sum(self.finalTfIdfMartix[token])

                for i in range (self.totalSentences):
                    if(self.finalTfIdfMartix[token][i] > 0 and self.label[i]==classLabel):
                        totalTokenPosOnGivenClass += self.finalTfIdfMartix[token][i]
                # if the token not in given class in all dataset
                # zero probability problem
                if(totalTokenPosOnGivenClass == 0):
                    likelihoodOfGivenClass = 1 / (totalNoOfToken + len(self.vocabulary))
                else:
                    likelihoodOfGivenClass = totalTokenPosOnGivenClass / totalNoOfToken
            # if the token not in dataset features
            # new word not known to daset (zero prob problem) 
            # likelihood =  1/total count of tokens in class C + len(vocab)
            else:
                likelihoodOfGivenClass = 1 / (totalTokenInGivenClass + len(self.vocabulary))

            finalLikelihood *= likelihoodOfGivenClass

        return finalLikelihood

nb = NaiveBayesClass()
sentence = "love this"
nb.calculateSentiment(sentence)