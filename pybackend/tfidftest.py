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
        tokenIdfValue = totalNoOfDoc / totalDocContainingTokenCount[token]    
        eachIdfValue.append(tokenIdfValue)
    
    finalIdfMatrix.append(eachIdfValue)

    return finalIdfMatrix
       

finalIdfMatrix = createIdfMatrix(sentences)
finalIdfMatrix = pd.DataFrame(finalIdfMatrix,columns=vocabulary)
print("IDF matrix")
print(finalIdfMatrix)
    
