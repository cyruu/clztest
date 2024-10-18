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

print("priorPositiveProbability",priorPositiveProbability)
print("priorNegativeProbability",priorNegativeProbability)

# likelihood of sentence for positive class
sentence = "bad hate love love this hate"
sentenceTokenized = sentence.split()

likelihoodOfPositiveClass = 1
likelihoodOfNegativeClass = 1

# positive likelihood

for token in sentenceTokenized:
    likelihoodOfTokenInPosClass = 0
    # calculate count of that token present in class(pos or neg)
    totalTokenPosLabelPos = 0
    totalNoOfToken = 0
    for i in range(len(label)):
        if(matrix[token][i] == 1 and label[i] == 1):
            totalTokenPosLabelPos += 1

    # total count of that token in all class (pos or neg)
    totalNoOfToken = sum(matrix[token])

    # zero probability problem if token not present in class (pos or neg)
    if(totalTokenPosLabelPos == 0):
        likelihoodOfTokenInPosClass = 1 / (totalNoOfToken + len(vocabulary))
    else:
        likelihoodOfTokenInPosClass = totalTokenPosLabelPos / totalNoOfToken
    
    # multiply each likelihood to calc total likelihood
    likelihoodOfPositiveClass *= likelihoodOfTokenInPosClass
    
# posterior probablility of positive class and sentence
posteriorProbOfPosClass = priorPositiveProbability * likelihoodOfPositiveClass
print("posterior prob of pos class: ", posteriorProbOfPosClass)



# negative likelihood
for token in sentenceTokenized:
    likelihoodOfTokenInNegClass = 0
    # calculate count of that token present in class(pos or neg)
    totalTokenPosLabelNeg = 0
    totalNoOfToken = 0
    for i in range(len(label)):
        if(matrix[token][i] == 1 and label[i] == 0):
            totalTokenPosLabelNeg += 1

    # total count of that token in all class (pos or neg)
    totalNoOfToken = sum(matrix[token])

    # zero probability problem if token not present in class (pos or neg)
    if(totalTokenPosLabelNeg == 0):
        likelihoodOfTokenInNegClass = 1 / (totalNoOfToken + len(vocabulary))
    else:
        likelihoodOfTokenInNegClass = totalTokenPosLabelNeg / totalNoOfToken
    
    # multiply each likelihood to calc total likelihood
    likelihoodOfNegativeClass *= likelihoodOfTokenInNegClass
    
# posterior prob of sentence in negative class
posteriorProbOfNegClass = priorNegativeProbability * likelihoodOfNegativeClass
print("posterior prob of neg class: ",posteriorProbOfNegClass)



