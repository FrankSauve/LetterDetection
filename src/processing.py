import os


def get_dataset(path):
    """
    Gets the features and labels of the dataset
    :param string path: The path the the dataset file after /datasets/
    :return: features, labels
    """
    with open(os.path.abspath(os.path.join(os.getcwd(), "../datasets/", path)), "r") as file:
        data = [line.split(',') for line in file.read().split('\n')][:-1]
    data = [[int(element) for element in row] for row in data]
    features = [d[:-1] for d in data]
    labels = [d[-1] for d in data]
    return features, labels


def get_test_dataset(path):
    """
    Gets a dataset that only has features
    :param string path: The path the the dataset file after /datasets/
    :return: features
    """
    with open(os.path.abspath(os.path.join(os.getcwd(), "../datasets/", path)), "r") as file:
        data = [line.split(',') for line in file.read().split('\n')][:-1]
    data = [[int(element) for element in row] for row in data]
    features = [d for d in data]
    return features
