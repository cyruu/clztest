import pandas as pd
from DataClass import DataClass
from CustonAlgorithm import CustomAlgorithm
from collections import Counter


dc = DataClass()
algo = CustomAlgorithm()
# Sample lemmatized sentences (replace with your data)
lemmatized_sentences = [
    "dog bite man",
    "man bite dog dog",
    "dog and man",
]
tokenizedSentences = [['dog', 'bite', 'man'], ['man', 'bite', 'dog', 'dog'], ['dog', 'and', 'man']]

[bagOfWords,allUniqueTokens] = algo.generateBagOfWords(lemmatized_sentences)
print(bagOfWords)
print(allUniqueTokens)

# # Step 1: Tokenize the sentences
# tokenized_sentences = [sentence.split() for sentence in lemmatized_sentences]
# vocabulary = sorted(set(word for sentence in tokenized_sentences for word in sentence))
# def create_bow(sentences, vocab):
#     bow = []
#     for sentence in sentences:
#         word_counts = Counter(sentence)
#         bow.append([word_counts.get(word, 0) for word in vocab])
#     return pd.DataFrame(bow, columns=vocab)

# # Step 4: Generate the BoW matrix
# bow_df = create_bow(tokenized_sentences, vocabulary)

# # Display the Bag of Words as a table
# print(bow_df) 

