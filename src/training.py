import os
from sklearn.naive_bayes import MultinomialNB


def get_training_dataset(path):
    with open(os.path.abspath(os.path.join(os.getcwd(), "../datasets/", path)), "r") as file:
        data = [line.split(',') for line in file.read().split('\n')][:-1]
    data = [[int(element) for element in row] for row in data]
    features = [d[:-1] for d in data]
    labels = [d[-1] for d in data]
    return features, labels

# MNB_Classifier = MultinomialNB()
# MNB_Classifier.fit()
