import pandas as pd


vocabulary = ["love","this","is","great","hate","bad"]
label = [1,1,0,0]
bagOfWords = [
    [1,1,0,0,0,0],
    [0,1,1,1,0,0],
    [0,1,0,0,1,0],
    [0,1,1,0,0,1]
]

matrix = pd.DataFrame(bagOfWords,columns=vocabulary)
matrix["label"] = label

totalSentences = len(label)
totalPositiveSentence = label.count(1)
totalNegativeSentece = label.count(0)

# prior probability for Positive
priorPositiveProbability = totalPositiveSentence/totalSentences
# prior probability for Negative
priorNegativeProbability = totalNegativeSentece/totalSentences


# likelihood of sentence for positive class
sentence = "love this"
sentenceTokenized = sentence.split()

def calculateLikelihood(sentenceTokenized,classLabel):
    finalLikelihood = 1
    for token in sentenceTokenized:
        likelihoodOfGivenClass = 0
        totalTokenPosOnGivenClass = 0
        totalNoOfToken = 0

        for i in range (len(label)):
            if(matrix[token][i] ==1 and label[i]==classLabel):
                totalTokenPosOnGivenClass += 1
        
        totalNoOfToken = sum(matrix[token])

        if(totalTokenPosOnGivenClass == 0):
            likelihoodOfGivenClass = 1 / (totalNoOfToken + len(vocabulary))
        else:
            likelihoodOfGivenClass = totalTokenPosOnGivenClass / totalNoOfToken

        finalLikelihood *= likelihoodOfGivenClass

    return finalLikelihood

likelihoodPositive = calculateLikelihood(sentenceTokenized,1)
likelihoodNegative = calculateLikelihood(sentenceTokenized,0)
print("likelihood poss: ",likelihoodPositive)
print("likelihood negg: ",likelihoodNegative)