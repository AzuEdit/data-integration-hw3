from sklearn import decomposition


def make_list(data_list, label_list):
    train_len = int(len(data_list) * 0.8)
    train_data_list = data_list[0:train_len]
    train_label_list = label_list[0:train_len]
    test_data_list = data_list[train_len:]
    test_label_list = label_list[train_len:]
    return train_data_list, train_label_list, test_data_list, test_label_list


def pca(train_data_list, test_data_list, to_data_list):
    model = decomposition.PCA(n_components='mle')
    model.fit(train_data_list + test_data_list + to_data_list)
    train_data_list = model.transform(train_data_list)
    test_data_list = model.transform(test_data_list)
    to_data_list = model.transform(to_data_list)
    return train_data_list, test_data_list, to_data_list
