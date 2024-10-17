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

print(priorPositiveProbability,priorNegativeProbability)

