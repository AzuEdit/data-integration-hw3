from query import query_star
from query import query_credit
import classify
import preprocess
import optimize


def process_star():
    useless_uid_list, data_list, label_list = query_star(False)
    print("查询星级评估训练集、测试集成功")
    uid_list, to_data_list, useless_label_list = query_star(True)
    print("查询星级评估待预测集成功")

    train_data_list, train_label_list, test_data_list, test_label_list = preprocess.make_list(data_list, label_list)
    train_data_list, test_data_list, to_data_list = preprocess.pca(train_data_list, test_data_list, to_data_list)
    print("星级评估数据预处理完成")

    # optimize.optimize(train_data_list, train_label_list, test_data_list, test_label_list)
    classify.rf("star", train_data_list, train_label_list, test_data_list, test_label_list, uid_list, to_data_list)
    # classify.dt("star", train_data_list, train_label_list, test_data_list, test_label_list, uid_list, to_data_list)
    # classify.nn("star", train_data_list, train_label_list, test_data_list, test_label_list, uid_list, to_data_list)
    # classify.svm("star", train_data_list, train_label_list, test_data_list, test_label_list, uid_list, to_data_list)
    # classify.nb("star", train_data_list, train_label_list, test_data_list, test_label_list, uid_list, to_data_list)


def process_credit():
    useless_uid_list, data_list, label_list = query_credit(False)
    print("查询信用等级评估训练集、测试集成功")
    uid_list, to_data_list, useless_label_list = query_credit(True)
    print("查询信用等级评估待预测集成功")

    train_data_list, train_label_list, test_data_list, test_label_list = preprocess.make_list(data_list, label_list)
    train_data_list, test_data_list, to_data_list = preprocess.pca(train_data_list, test_data_list, to_data_list)
    print("信用等级评估数据预处理完成")

    # optimize.optimize(train_data_list, train_label_list, test_data_list, test_label_list)
    classify.rf("credit", train_data_list, train_label_list, test_data_list, test_label_list, uid_list, to_data_list)
    # classify.dt("credit", train_data_list, train_label_list, test_data_list, test_label_list, uid_list, to_data_list)
    # classify.nn("credit", train_data_list, train_label_list, test_data_list, test_label_list, uid_list, to_data_list)
    # classify.svm("credit", train_data_list, train_label_list, test_data_list, test_label_list, uid_list, to_data_list)
    # classify.nb("credit", train_data_list, train_label_list, test_data_list, test_label_list, uid_list, to_data_list)


def main():
    process_star()
    process_credit()


if __name__ == '__main__':
    main()
