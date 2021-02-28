
## 心得笔记


### 淘宝定向广告演化

LR --(非线性能力)--> MLR --(深度学习)--> DNN --(兴趣捕捉)--> DIN --(兴趣演化)--> DIEN --(兴趣会话)--> DSIN

演化规律：
* 降低信息损失
* 先有洞察，再有拟合
* 模型是为了更好的拟合洞察
* 工程中提出Dice，Mini-Batch Aware Regularization，auxiliary loss
* 随着模型越来越复杂，越需要并行计算（GPU）


### Attention机制
* 在对用户行为的embedding计算上引入了attention network (也称为Activation Unit) 
* 把用户历史行为特征进行embedding操作，视为对用户兴趣的表示，之后通过Attention Unit，对每个兴趣表示赋予不同的权值
* Attention Weight是由用户历史行为和候选广告进行匹配计算得到的，对应着洞察（用户兴趣的Diversity，以及Local Activation）


