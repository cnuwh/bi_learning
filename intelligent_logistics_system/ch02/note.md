

# 常见的回归算法
* 线性回归 / 逻辑回归
* 多项式回归 Polynomial Regression
* 岭回归 Ridge Regression
* 套索回归 Lasso Regression
* 弹性回归 ElasticNet Regression
* 分类用于回归：SVM，KNN，CART
* 集成学习：RF，GBDT, XGBoost, LightGBM

多项式是一种常用的特征构造方法， 岭回归和套索回归的混合技术，同时使用L2和L1正则


# 模型融合
* 回归任务中的加权融合

根据各个模型的最终预测表现分配不同的权重，比如准确率高的模型给予更高的权重，准确率低的模型给予较小的权重

* 分类任务中的Voting

Voting策略，即选择所有模型输出结果中，最多的那个类（少数服从多数）
