import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

csv = pd.read_csv('iris.csv')

# 열 이름으로 분할 가능
csv_data = csv[["sepal.length","sepal.width","petal.length","petal.width"]]
csv_label = csv["variety"]

# 자동 분할 메소드 사용 (train_test_split)
# https://990427.tistory.com/67
train_data, test_data, train_label, test_label = \
    train_test_split(csv_data, csv_label)


clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

# 정확도 검사 (모듈 사용)
ac_score = metrics.accuracy_score(test_label, pre)
print("match percent : {}%".format(int(ac_score*100)))
