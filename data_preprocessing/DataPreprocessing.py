
# importing some standard libraries 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import urllib


# Importing Datasets..
# Method 1: 
# URL for the Pima Indians Diabetes dataset (UCI Machine Learning Repository)

url = "http://goo.gl/j0Rvxq"
# download the file
raw_data = urllib.urlopen(url)
# load the CSV file as a numpy matrix
dataset = np.loadtxt(raw_data, delimiter=",")
print(dataset.shape)
# separate the data from the target attributes

#Method 2:
# Importing the data set using Pandas

dataset=pd.read_csv('Data.csv')
df = pd.read_csv(Location, header=None)
df = pd.read_csv(Location, names=['Names','Births'])

#Or
Location = r'C:\Users\david\notebooks\update\births1880.txt'
df = pd.read_csv(Location)

#Conversion to excel
df.to_excel('DimDate.xls', index=False)

#Conversion to csv
df.to_csv('DimDate.txt', index=False)

#Seperating Dependent and Independent Coloumns(Standard Convention)
#You Can Modify Accordingly
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,3].values


#You can also use pandas to initialize the missing data as NaN but that would not solve  our problem
# Taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])


#remove dataset
import os
os.remove(Location)

sort
# Method 1:
Sorted = df.sort_values(['Births'], ascending=False)
df.to_csv('births1880.txt',index=False,header=False)

#Splitting of data sets into training and test data sets using sklearn
from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=#{U can enter the ratio},random_state=0)

#Feature Scaling

from sklearn.preprocessing import StandardScaler
Sc_X=StandardScaler()
X_train=Sc_X.fit_transform(X_train)
X_test=Sc_X.transform(X_test)





