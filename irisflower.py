#!/usr/bin/python3

from sklearn import tree
import matplotlib.pyplot as plt
import time
from sklearn.datasets import load_iris
import numpy as np
# load iris data
iris=load_iris()
#print flower name
# f_name=iris.target_names
# print(f_name)
#print feature of flower
# f_feature=iris.feature_names
# print(f_feature)
#loading feature data
f_feature_data=iris.data
# print(f_feature_data)

realdataset=iris.target
# trained and tested data of setosa(output)
setosa=realdataset[0:50]
s_trained_data=setosa[0:49]
s_tested_data=setosa[-1]
# trained and tested data of versicolor


versicolor=realdataset[50:100]
# print(versicolor)
vc_trained_data=versicolor[0:49]
vc_tested_data=versicolor[-1]
#trained and tested data of versinica
virginica=realdataset[100:150]
vn_trainded_data=virginica[0:49]
vn_tested_data=virginica[-1]


print("************************************")
print(type(s_trained_data))
#plt.xlabel("Setosa")
#plt.ylabel("Versicolor")
#plt.ylabel("virginica")
plt.title("IrisFlower")
x=f_feature_data[0:50]
y=f_feature_data[50:100]
x1=f_feature_data[100:150]
plt.scatter(x,y,label="Setosa",marker="*",color='g')
plt.scatter(y,x1,label="Versicolor",marker="*",color='b')
plt.scatter(x,x1,label="versinica",marker="*",color='k')
plt.legend()
plt.show()