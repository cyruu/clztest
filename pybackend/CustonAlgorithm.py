
import pandas as pd
class CustomAlgorithm:

    # constructor
    def __init__(self):
        self.tokenCountDictionaryList = []
        self.allUniqueTokens = []
        pass

    # main generate bow
    # 1. generate 2D array of sentences as words
    # 2. generate list of all unique tokens from all sentences in sorted form
    # 3. count number of words repeated in each tokenizedSentence as list of dictionary
    # ----4. generate Bag Of Words
    #       i. iterate through each tokenizedSentence
    #      ii. count number of words repeated in that tokenizedSentence
    def generateBagOfWords(self,sentences):
        tokenizedSentences = self.generateTokenizedSentences(sentences)
        self.allUniqueTokens = self.generateListOfUniqueTokensInAllSentences(tokenizedSentences)
        self.tokenCountDictionaryList = self.generateTokenCountDictionaryList(tokenizedSentences)
        
        bagOfWords = []
        for tokenDictionary in self.tokenCountDictionaryList:
            # Create a row for each sentence based on the count of each word in the vocab
            bagOfWords.append([tokenDictionary.get(word, 0) for word in self.allUniqueTokens])
        return [bagOfWords,self.allUniqueTokens]
            
            # oneRowBagOfWords = [] 
        # return pd.DataFrame(bow, columns=vocab)
        
        # print(self.tokenCountDictionaryList)


    # 1. generate 2D array of sentences as words
    # ['i like','how to'] into
    # [['i','like'],['how','to']]
    def generateTokenizedSentences(self,sentences):

        tokenizedSentences = []
        for sentence in sentences:
            tokenizedSentence = sentence.split()
            tokenizedSentences.append(tokenizedSentence)
        
        return tokenizedSentences
    
    # 2. create a list of all the unique words of all sentences
    # a.k.a (Vocabulary)
    def generateListOfUniqueTokensInAllSentences(self,tokenizedSentences):
        allUniqueTokens = set()
        for tokenizedSentence in tokenizedSentences:
            for token in tokenizedSentence:
                allUniqueTokens.add(token)
        
        return sorted(list(allUniqueTokens))
    
    
    # generateTokenCountDictionaryList
    def generateTokenCountDictionaryList(self,tokenizedSentences):
        tokenCountDictionaryList = []
        for tokenizedSentence in tokenizedSentences:
            tokenCountDictionary = {}

            for token in tokenizedSentence:
                if token in tokenCountDictionary:
                    tokenCountDictionary[token] += 1
                else:
                    tokenCountDictionary[token] = 1
            
            tokenCountDictionaryList.append(tokenCountDictionary)
        return tokenCountDictionaryList