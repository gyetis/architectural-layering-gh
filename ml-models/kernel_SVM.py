__author__="GizemYetis, OzanYetkin, KongpyungMoon & Ozkan Kilic"
__mail__="yetis.gizem@metu.edu.tr, ozan.yetkin@metu.edu.tr, kpmoon@gmail.com & okilic@ybu.edu.tr"
__institution__="Middle East Technical University, Yildirim Beyazit University"

from Grasshopper import DataTree
import scriptcontext
np = scriptcontext.sticky['numpy']
sk = scriptcontext.sticky['sklearn']

data_list=[list(i) for i in training_set.Branches]
x_train=[]
y_train=[]
for d in range(data_list.Count): 
    x_train.append(data_list[d][:len(training_set.Branches[d])-1])
    y_train.append(data_list[d][len(training_set.Branches[d])-1:])

test_list=[list(i) for i in test_set.Branches]
x_test=[]
y_test=[]
for d in range(test_list.Count): 
    x_test.append(test_list[d][:len(test_set.Branches[d])-1])
    y_test.append(test_list[d][len(test_set.Branches[d])-1:])
for row in x_test:
    for k in (0,1,2):
        row[k] = float(row[k])

skpp = scriptcontext.sticky['sklearn.preprocessing']
labelencoder_y = skpp.LabelEncoder()
y_train = labelencoder_y.fit_transform(y_train)
y_test = labelencoder_y.fit_transform(y_test)

sc = skpp.StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

sklm=scriptcontext.sticky['sklearn.svm']
classifier = sklm.SVC(kernel = 'rbf', random_state = None)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)

skm=scriptcontext.sticky['sklearn.metrics']
cm = skm.confusion_matrix(y_test, y_pred)

yp=np.ndarray.tolist(labelencoder_y.inverse_transform(y_pred))
yt=np.ndarray.tolist(labelencoder_y.inverse_transform(y_test))

print(yp)
print(yt)
