# Apriori

# We will NOT import and use any liberaries.
# We will be using function from an external file "apyori.py" having emplimentation of Apriori algorithm, fetched from python software foundation.

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Importing database
# We have passed "header = None" below to tell python that there is no column headings (Headers).
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)

# Data Preprocessing
# The Apriori algorithm wants input as a list of lists, so converting into list of list.
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

# Training the Apriori model on the dataset
# We will NOT import and use any liberaries.
# We will be using function from an external file "apyori.py" having emplimentation of Apriori algorithm, fetched from python software foundation.
from apyori import apriori
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)

# Visualising the results
results = list(rules)
print(results)