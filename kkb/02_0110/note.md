
## 知识点总结

prophet是Facebook开源的时间序列预测工具： https://facebook.github.io/prophet/

prophet的优势：
* 处理数据丢失问题
* 趋势迁移问题（shifts in the trend）
* 异常的数据点（outliers）

prophet模型： y(t)=g(t)+s(t)+h(t)+e
* g(t)代表趋势项，用来表示时间序列中非周期性的变化
* s(t)代表周期项，用来表示时间序列中的周期变化
* h(t)代表活动效果项，用来表达时间序列中的一些异常活动，例节假日，购物节等
* e 用来表示不能被模型所描述的异常误差


## 学习心得
* prophet与ARMA、ARIMA类似，只能处理单特征时间序列，无法处理多特征时间序列
* prophet拟合速度较快，一般在1~5秒，可以快速做一个baseline出来
* prophet中节假日相关的参数比较好调，只需要罗列出时间段内的节假日日期即可；饱和增长相关的参数不太好调，一般无法得到时间序列准确的上下限

