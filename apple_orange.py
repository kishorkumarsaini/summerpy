#!/usr/bin/python3
from sklearn import tree
 
# apple and orange smooth=1 and bumpy=1
features=[[110,0],[120,0],[130,1],[140,1]]

output=["apple","apple","orange","orange"]

#now loading the DecisionTreeCalssifier
algo=tree.DecisionTreeClassifier()
#now training the features and output set
trained=algo.fit(features,output)
#testing trained model and Q & A
result=trained.predict([[130,1]])
#print result
print(result)
