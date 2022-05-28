from sklearn.svm import SVC
from sklearn import neural_network
from sklearn import tree
from sklearn import naive_bayes
from sklearn import ensemble


def svm(star_or_credit, train_data_list, train_label_list, test_data_list, test_label_list, uid_list,
        to_data_list):
    model = SVC()
    model.fit(train_data_list, train_label_list)
    print('使用SVC，对于' + star_or_credit + '训练集准确率：', model.score(train_data_list, train_label_list))
    print('使用SVC，对于' + star_or_credit + '测试集准确率：', model.score(test_data_list, test_label_list))
    output(model, star_or_credit, uid_list, to_data_list)


def nn(star_or_credit, train_data_list, train_label_list, test_data_list, test_label_list, uid_list,
       to_data_list):
    model = neural_network.MLPClassifier(max_iter=1000)
    model.fit(train_data_list, train_label_list)
    print('使用神经网络，对于' + star_or_credit + '训练集准确率：', model.score(train_data_list, train_label_list))
    print('使用神经网络，对于' + star_or_credit + '测试集准确率：', model.score(test_data_list, test_label_list))
    output(model, star_or_credit, uid_list, to_data_list)


def dt(star_or_credit, train_data_list, train_label_list, test_data_list, test_label_list, uid_list,
       to_data_list):
    model = tree.DecisionTreeClassifier(criterion='gini', min_samples_leaf=3)
    model.fit(train_data_list, train_label_list)
    print('使用决策树，对于' + star_or_credit + '训练集准确率：', model.score(train_data_list, train_label_list))
    print('使用决策树，对于' + star_or_credit + '测试集准确率：', model.score(test_data_list, test_label_list))
    output(model, star_or_credit, uid_list, to_data_list)


def nb(star_or_credit, train_data_list, train_label_list, test_data_list, test_label_list, uid_list,
       to_data_list):
    model = naive_bayes.GaussianNB()
    model.fit(train_data_list, train_label_list)
    print('使用朴素贝叶斯分类器，对于' + star_or_credit + '训练集准确率：', model.score(train_data_list, train_label_list))
    print('使用朴素贝叶斯分类器，对于' + star_or_credit + '测试集准确率：', model.score(test_data_list, test_label_list))
    output(model, star_or_credit, uid_list, to_data_list)


def rf(star_or_credit, train_data_list, train_label_list, test_data_list, test_label_list, uid_list,
       to_data_list):
    model = ensemble.RandomForestClassifier(n_estimators=20, random_state=0)
    model.fit(train_data_list, train_label_list)
    print('使用随机森林，对于' + star_or_credit + '训练集准确率：', model.score(train_data_list, train_label_list))
    print('使用随机森林，对于' + star_or_credit + '测试集准确率：', model.score(test_data_list, test_label_list))
    output(model, star_or_credit, uid_list, to_data_list)


def output(model, star_or_credit, uid_list, to_data_list):
    to_label_list = model.predict(to_data_list)
    file = open(star_or_credit + '.csv', "w", encoding='utf-8')
    for i in range(0, len(uid_list)):
        file.write(uid_list[i] + ',' + to_label_list[i] + '\n')
    file.close()
