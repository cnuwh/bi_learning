# 在CTR点击率预估中，使用GBDT+LR的原理是什么？
* 具有stacking思想的二分类器模型，用来解决二分类问题
* 通过GBDT将特征进行组合，然后传入给线性分类器
* LR对GBDT产生的输入数据进行分类（使用L1正则化防止过拟合）

# GBDT和随机森林都是基于树的算法，它们有什么区别？

* 随机森林采用的bagging思想，而GBDT采用的boosting思想。
* 组成随机森林的树可以是分类树，也可以是回归树；而GBDT只能由回归树组成。
* 组成随机森林的树可以并行生成；而GBDT只能是串行生成。
* 对于最终的输出结果而言，随机森林采用多数投票等；而GBDT则是将所有结果累加起来，或者加权累加起来。
* 随机森林对异常值不敏感；GBDT对异常值非常敏感。
* 随机森林对训练集一视同仁；GBDT是基于权值的弱分类器的集成。
* 随机森林是通过减少模型方差提高性能；GBDT是通过减少模型偏差提高性能。