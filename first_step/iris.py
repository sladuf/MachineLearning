from sklearn import svm, metrics
import random, re

csv = []

with open('iris.csv', 'r', encoding='utf-8') as fp:
    for line in fp:
        line = line.strip()
        cols = line.split(',')

        # 숫자들은 float type으로 변환하여 저장
        fn = lambda n : float(n) if re.match(r'^[0-9\.]+$', n) else n
        cols = list(map(fn, cols))
        csv.append(cols)

# 헤더 제거
del csv[0]

random.shuffle(csv)

total_len = len(csv)
train_len = int(total_len *2 / 3) # 데이터의 2/3만 학습하고, 1/3은 test로 사용
train_data =[]
train_label = []
test_data = []
test_label = []

for i in range(total_len):
    data = csv[i][0:4] # flower info
    label = csv[i][4] # type of flower
    if i < train_len :
        train_data.append(data)
        train_label.append(label)

    else:
        test_data.append(data)
        test_label.append(label)


clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

test_len = len(test_label)

# 정확도 검사
match = 0
for i in range(test_len):
    if pre[i] == test_label[i]:
        match +=1

print("match percent : {}%".format(int((match/test_len)*100)))

# 검사 모듈 사용
ac_score = metrics.accuracy_score(test_label, pre)
print(ac_score)
