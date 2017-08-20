import sklearn
from sklearn import tree
features = [[140,1],[130,1],[150,1],[170,0]]
labels = [0,0,1,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print ("the guess: "+str(clf.predict([[160,0]])))
result = clf.predict([[160,0]])
if result[0]==1:
	print("correct")
