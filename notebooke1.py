#Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

diabetes=datasets.load_diabetes()



#goal is to predict the progression of diabetes based on these input features

X=diabetes.data
y=diabetes.target

print(X)
print(y)