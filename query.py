import requests

SSL_VERIFY = False
host = 'http://127.0.0.1:8123'


def query_star(predict_flag):
    query_dict = {
        'query': "select * from"
                 "(select s.uid,star_level,sum(all_bal)/count(*),(sum(a.avg_mth)+sum(ac.avg_mth))/(2*count(*)),"
                 "(sum(a.avg_qur)+sum(ac.avg_qur))/(2*count(*)),(sum(a.avg_year)+sum(ac.avg_year))/(2*count(*)),"
                 "sum(sa_bal)/count(*),sum(td_bal)/count(*),sum(fin_bal)/count(*),sum(sa_crd_bal)/count(*),"
                 "sum(td_crd_bal)/count(*),sum(ntc_bal)/count(*),sum(td_3m_bal)/count(*),sum(td_6m_bal)/count(*),"
                 "sum(td_1y_bal)/count(*),sum(td_2y_bal)/count(*),sum(td_3y_bal)/count(*),sum(td_5y_bal)/count(*),"
                 "sum(oth_td_bal)/count(*),sum(cd_bal)/count(*),sum(acct_bal)/count(*),sum(bal)/count(*) from "
                 "dm.pri_star_info s inner join dm.pri_cust_asset_info a on s.uid=a.uid inner join "
                 "dm.pri_cust_asset_acct_info ac on a.uid=ac.uid group by s.uid,star_level) "
                 "where star_level!='-1' "
    }
    if predict_flag:
        query_dict = {
            'query': "select * from"
                     "(select s.uid,star_level,sum(all_bal)/count(*),(sum(a.avg_mth)+sum(ac.avg_mth))/(2*count(*)),"
                     "(sum(a.avg_qur)+sum(ac.avg_qur))/(2*count(*)),(sum(a.avg_year)+sum(ac.avg_year))/(2*count(*)),"
                     "sum(sa_bal)/count(*),sum(td_bal)/count(*),sum(fin_bal)/count(*),sum(sa_crd_bal)/count(*),"
                     "sum(td_crd_bal)/count(*),sum(ntc_bal)/count(*),sum(td_3m_bal)/count(*),sum(td_6m_bal)/count(*),"
                     "sum(td_1y_bal)/count(*),sum(td_2y_bal)/count(*),sum(td_3y_bal)/count(*),sum(td_5y_bal)/count(*),"
                     "sum(oth_td_bal)/count(*),sum(cd_bal)/count(*),sum(acct_bal)/count(*),sum(bal)/count(*) from "
                     "dm.pri_star_info s inner join dm.pri_cust_asset_info a on s.uid=a.uid inner join "
                     "dm.pri_cust_asset_acct_info ac on a.uid=ac.uid group by s.uid,star_level) "
                     "where star_level='-1' "
        }
    return query(query_dict)


def query_credit(predict_flag):
    query_dict = {
        'query': "select * from("
                 "select c.uid,credit_level,sum(all_bal)/count(*),sum(bad_bal)/count(*),sum(due_intr)/count(*),"
                 "sum(norm_bal)/count(*),sum(delay_bal)/count(*) "
                 "from dm.pri_credit_info c "
                 "inner join dm.pri_cust_liab_info l on c.uid=l.uid "
                 "group by c.uid, c.credit_level)"
                 "where credit_level!='-1'"
    }
    if predict_flag:
        query_dict = {
            'query': "select * from("
                     "select c.uid,credit_level,sum(all_bal)/count(*),sum(bad_bal)/count(*),sum(due_intr)/count(*),"
                     "sum(norm_bal)/count(*),sum(delay_bal)/count(*) "
                     "from dm.pri_credit_info c "
                     "inner join dm.pri_cust_liab_info l on c.uid=l.uid "
                     "group by c.uid, c.credit_level)"
                     "where credit_level='-1'"
        }
    return query(query_dict)


def query(query_dict):
    r = requests.post(host, params=query_dict, verify=SSL_VERIFY)
    info_list = r.text.strip().split('\n')
    uid_list = []
    data_list = []
    label_list = []
    for info in info_list:
        specific_info = info.split('\t')
        uid_list.append(specific_info[0])
        label_list.append(specific_info[1])
        data = []
        for i in range(2, len(specific_info)):
            data.append(specific_info[i])
        data_list.append(data)
    return uid_list, data_list, label_list
