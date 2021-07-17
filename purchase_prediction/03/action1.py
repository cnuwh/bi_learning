import random
import math
import operator
import pandas as pd

file_path = "user_taggedbookmarks-timestamps.dat"
records = {}
train_data = dict()
test_data = dict()
user_tags = dict()
tag_items = dict()
user_items = dict()

################# NormTagBased ###################

def addValueToMat(mat, index, item, value=1):
    if index not in mat:
        mat.setdefault(index, {})
        mat[index].setdefault(item, value)
    else:
        if item not in mat[index]:
            mat[index][item] = value
        else:
            mat[index][item] += value

def load_data():
    df = pd.read_csv(file_path, sep='\t')
    for i in range(len(df)):
        uid = df['userID'][i]
        iid = df['bookmarkID'][i]
        tag = df['tagID'][i]
        records.setdefault(uid, {})
        records[uid].setdefault(iid, [])
        records[uid][iid].append(tag)

def train_test_split(ratio, seed=100):
    random.seed(seed)
    for u in records.keys():
        for i in records[u].keys():
            if random.random() < ratio:
                test_data.setdefault(u, {})
                test_data[u].setdefault(i, [])
                for t in records[u][i]:
                    test_data[u][i].append(t)
            else:
                train_data.setdefault(u, {})
                train_data[u].setdefault(i, [])
                for t in records[u][i]:
                    train_data[u][i].append(t)

def initStat():
    records = train_data
    for u, items in records.items():
        for i, tags in items.items():
            for tag in tags:
                addValueToMat(user_tags, u, tag, 1)
                addValueToMat(tag_items, tag, i, 1)
                addValueToMat(user_items, u, i, 1)

def recommend(user, N):
    recommend_items = dict()
    tagged_items = user_items[user]
    for tag, wut in user_tags[user].items():
        for item, wti in tag_items[tag].items():
            if item in tagged_items:
                continue

            if item not in recommend_items:
                recommend_items[item] = wut * wti
            else:
                recommend_items[item] = recommend_items[item] + wut * wti
    return sorted(recommend_items.items(), key=operator.itemgetter(1), reverse=True)[0:N]

def precisionAndRecall(N):
    hit = 0
    h_recall = 0
    h_precision = 0
    for user, items in test_data.items():
        if user not in train_data:
            continue
        rank = recommend(user, N)
        for item, rui in rank:
            if item in items:
                hit = hit + 1
        h_recall = h_recall + len(items)
        h_precision = h_precision + N
    return (hit / (h_precision * 1.0)), (hit / (h_recall * 1.0))

def testRecommend():
    print("%3s %10s %10s" % ('N', "精确率", '召回率'))
    for n in [5, 10, 20, 40, 60, 80, 100]:
        precision, recall = precisionAndRecall(n)
        print("%3d %10.3f%% %10.3f%%" % (n, precision * 100, recall * 100))

load_data()
train_test_split(0.2)
initStat()
testRecommend()


################# TagBased-TFIDF ###################
file_path = "user_taggedbookmarks-timestamps.dat"
records = {}
train_data = dict()
test_data = dict()
user_tags = dict()
tag_users = dict()
tag_items = dict()
user_items = dict()


def load_data():
    df = pd.read_csv(file_path, sep='\t')
    for i in range(len(df)):
        uid = df['userID'][i]
        iid = df['bookmarkID'][i]
        tag = df['tagID'][i]
        records.setdefault(uid,{})
        records[uid].setdefault(iid,[])
        records[uid][iid].append(tag)

def train_test_split(ratio, seed=100):
    random.seed(seed)
    for u in records.keys():
        for i in records[u].keys():
            if random.random()<ratio:
                test_data.setdefault(u,{})
                test_data[u].setdefault(i,[])
                for t in records[u][i]:
                    test_data[u][i].append(t)
            else:
                train_data.setdefault(u,{})
                train_data[u].setdefault(i,[])
                for t in records[u][i]:
                    train_data[u][i].append(t)

def addValueToMat(mat, index, item, value=1):
    if index not in mat:
        mat.setdefault(index,{})
        mat[index].setdefault(item,value)
    else:
        if item not in mat[index]:
            mat[index][item] = value
        else:
            mat[index][item] += value

def initStat():
    records=train_data
    for u,items in records.items():
        for i,tags in items.items():
            for tag in tags:
                addValueToMat(user_tags, u, tag, 1)
                addValueToMat(tag_users, tag, u, 1)
                addValueToMat(tag_items, tag, i, 1)
                addValueToMat(user_items, u, i, 1)


def recommend(user, N):
    recommend_item=dict()
    tagged_items = user_items[user]
    for tag, utn in user_tags[user].items():
        for item, wti in tag_items[tag].items():
            if item in tagged_items:
                continue
            if item not in recommend_item:
                recommend_item[item] = utn * utn / math.log(1 + sum(tag_users[tag].values()))
            else:
                recommend_item[item] += utn * utn / math.log(1 + sum(tag_users[tag].values()))
    return sorted(recommend_item.items(), key=operator.itemgetter(1), reverse=True)[0:N]


def precisionAndRecall(N):
    hit = 0
    h_recall = 0
    h_precision = 0
    for user,items in test_data.items():
        if user not in train_data:
            continue
        rank = recommend(user, N)
        for item,rui in rank:
            if item in items:
                hit = hit + 1
        h_recall = h_recall + len(items)
        h_precision = h_precision + N
    return (hit/(h_precision*1.0)), (hit/(h_recall*1.0))


def testRecommend():
    print("%3s %10s %10s" % ('N',"精确率",'召回率'))
    for n in [5,10,20,40,60,80,100]:
        precision,recall = precisionAndRecall(n)
        print("%3d %10.3f%% %10.3f%%" % (n, precision * 100, recall * 100))


load_data()
train_test_split(0.2)
initStat()
testRecommend()


'''
====================== NormTagBased output =====================
  N        精确率        召回率
  5      0.829%      0.355%
 10      0.633%      0.542%
 20      0.512%      0.877%
 40      0.381%      1.304%
 60      0.318%      1.635%
 80      0.276%      1.893%
100      0.248%      2.124%

====================== TagBased-TFIDF output =====================
N        精确率        召回率
5       0.739%      0.316%
10      0.521%      0.446%
20      0.378%      0.647%
40      0.283%      0.968%
60      0.234%      1.203%
80      0.216%      1.481%
100     0.195%      1.673%
'''