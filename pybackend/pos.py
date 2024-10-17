

import json

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
from DataClass import DataClass
from CustonAlgorithm import CustomAlgorithm

dc = DataClass()
algo = CustomAlgorithm()

sentences = ["He's don't ! like12 reading won't 3  books.","This is buying ongoing product","Sam is going abroad this saturday and reading in a flying emergency flights"]