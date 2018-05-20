#!/usr/bin/python3

from sklearn import tree
import matplotlib.pyplot as plt
import time
from sklearn.datasets import load_iris
import numpy as np


iris=load_iris()
#print(dir(iris))
irisdata=iris.data
#print(irisdata)
#  features Training  iris tree dataset
f_trainig=np.delete(irisdata,[49,99,149],axis=0)
#print(f_trainig)
# features Testing iris tree dataset

f_testing=irisdata[[49,99,149]]
#print(f_testing)


print("***************output data*******************")

# target  datset of iris tree
target_data=iris.target
#print(target_data)
#training  output dataset
output_trainigdata=np.delete(target_data,[49,99,149],axis=0)
#print(output_trainigdata)
#print(output_trainigdata.shape)
# training output dataset
output_testingdata=target_data[[49,99,149]]
print(output_testingdata)
# algo of decision tree  classifier
algo=tree.DecisionTreeClassifier()
# trained tne data 
trained=algo.fit(f_trainig,output_trainigdata)
# predication 
result=trained.predict(f_testing)
print(result)


