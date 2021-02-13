
## 知识点总结


### Airbnb List Embedding（房源嵌入）：
1. 将每个房源 => 房源embedding
2. 数据集由 N 个用户的点击会话 (Session) 组成，其中每个会话定义为一个由用户点击的 M个房源 id 组成的的不间断序列
3. 只要用户连续两次点击时间间隔超过30分钟，就认为是一个新的Session
4. 目标是通过集合S，学习出每个房源listing的d维（ 32 维）embedding表示，让相似listing在embedding空间中距离更近
5. 借鉴了word2vec中的skip-gram算法
6. 房源embedding，把每个用户连续点击过的房源Session看做一个句子，每个房源当做word，训练出房源的embedding

### Word2Vec的两种模式：
1. Skip-Gram，跳字模型，给定input word预测上下文
2. CBOW，连续词袋模型，给定上下文，预测input word（与Skip-Gram相反）

### List Embedding的冷启动：
* 每天Airbnb都有新的房源产生，冷启动在所难免
* 房主上传新房源时需要上传3个特征，位置，价格，房源类型（包括整个房源，独立房间，合住房间3个类别）
* 在和新上传房源具有相同类型和相同价格区间的房源中，找到3个地理位置最接近的房源，用这3个房源的embedding求平均作为新房源的embedding
* 能覆盖到98%的新Listing


## 学习心得
本课主要学习了Word2vec & embedding的思想，他们属于特征处理范畴，是特征处理的一种方法，与SVD或者PCA等一些常用的降维方法类似
