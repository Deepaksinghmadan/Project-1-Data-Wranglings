
# coding: utf-8

# In[1]:

import numpy as np #wrangling
import pandas as pd
import random as rnd
import seaborn as sns #visualisation
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression,SGDClassifier,Perceptron
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier


# In[3]:

train_df = pd.read_csv("C:\\Users\\deepak\\Downloads\\train.csv")
test_df = pd.read_csv("C:\\Users\\deepak\\Downloads\\test.csv")
combine = [train_df,test_df]


# In[5]:

print(train_df.columns.values)


# In[6]:

train_df.head()


# In[7]:

train_df.tail()


# In[ ]:



