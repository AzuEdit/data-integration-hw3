from sklearn import ensemble


def optimize(train_data_list, train_label_list, test_data_list, test_label_list):
    for i in range(0, 100, 10):
        if i == 0:
            j = 1
        else:
            j = i
        model = ensemble.RandomForestClassifier(n_estimators=20, random_state=0)
        model.fit(train_data_list, train_label_list)
        print("n_estimators: ", j, " 准确率: ", model.score(test_data_list, test_label_list))
