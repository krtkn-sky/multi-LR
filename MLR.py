import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Data.csv')
#print(dataset)

X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

#print(X)
#print(y)