# Thinking1 逻辑回归的假设条件是怎样的？

* 假设1：数据服从伯努利分布
* 假设2：正类的概率由sigmoid函数计算

# Thinking2 逻辑回归的损失函数是怎样的？


l(theta) = log L(theta) = sum (y<sup>(i)</sup>log h<sub>theta</sub>(x<sup>(i)</sup>) + (1-y<sup>(i)</sup>log(1-h<sub>theta</sub>(x<sup>(i)</sup>))))

# Thinking3 逻辑回归如何进行分类？
设定一个阈值，判断正类概率是否大于该阈值，一般阈值是0.5，所以只用判断正类概率是否大于0.5即可


# Thinking4 为什么在训练中需要将高度相关的特征去掉？
* 可解释性更好
* 提高训练的速度，特征多了，会增大训练的时间
