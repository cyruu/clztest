import pandas as pd

sentences = [
    "i love food",
    "great service",
    "i hate ambiance"
]

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
    tokenAppearedInDocCount = {}

    # each sentence (doc)
    for sentence in sentences:
        eachRowTfMatrix = []
        tokenizedSentence = sentence.split()
        # create count dictionary for each sentence
        for token in tokenizedSentence:
            totalTokenApperedInDoc = tokenizedSentence.count(token)
            if(token in tokenAppearedInDocCount):
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
    for sentence in sentences:
        tokenizedSentence = sentence.split()
