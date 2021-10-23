from sklearn import model_selection, svm, metrics

def load_csv(fname):
    labels = []
    images = []

    # mnist_to_csv 참고
    with open(fname, "r") as f :
        for line in f:
            cols = line.split(",")
            if len(cols) < 2 : continue
            # data line의 0번 (label)
            labels.append(int(cols.pop(0)))
            # data line의 1~256번 (pixel)
            vals = list(map(lambda n: int(n) / 256, cols))
            images.append(vals)
    
    return {"labels" : labels, "images" : images}

data = load_csv("./mnist/data/train.csv")
test = load_csv("./mnist/data/test.csv")

clf = svm.SVC()
clf.fit(data["images"], data["labels"])

pre = clf.predict(test["images"])

as_score = metrics.accuracy_score(test["labels"], pre)
cl_report = metrics.classification_report(test["labels"], pre)
print("match percent : {}%".format(int(as_score*100)))
print("REPORT")
print(cl_report)
