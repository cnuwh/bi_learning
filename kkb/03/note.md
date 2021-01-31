
## 知识点总结

### 时间序列规则/时间序列周期因子/季节因子

很多数据都具有明显的周期性，可以用简单的统计量来作为特征（中位数、均值、临近数据等），从中这种周期性中提取出有用的信息。使用周期因子进行预测的步骤：

1. 获得周期因子（weekday）获得星期几的均值，再除以整体均值
2. 计算base
3. 使用base * 周期因子进行预测

### 正则表达式
略（个人对正则表达式比较熟悉，这里不展开了）

### TF-IDF

什么是TF-IDF：
TF：Term Frequency，词频
一个单词的重要性和它在文档中出现的次数呈正比。

TF = 单词次数/文档中总单词数

IDF：Inverse Document Frequency，逆向文档频率
一个单词在文档中的区分度。这个单词出现的文档数越少，区分度越大，IDF越大

IDF = log(文档总数/(单词出现的文档数 + 1))

### TextRank

TextRank流程：
* Step1，进行分词和词性标注，将单词添加到图中
* Step2，出现在一个窗口中的词形成一条边
* Step3，基于PageRank原理进行迭代（20-30次）
* Step4，顶点（词）按照分数进行排序，可以筛选指定的词性


TextRank生成摘要的原理：
* 每个句子作为图中的节点
* 如果两个句子相似，则节点之间存在一条无向有权边
* 相似度=同时出现在两个句子中的单词的个数/句子中单词个数求对数之和
（分母使用对数可以降低长句在相似度计算上的优势）


## 学习心得

搜遍google、bing、百度、知乎、简书，没有找到周期因子&日期因子相关的推导过程，所以自己尝试推导一下。

符号定义：
* f<sub>d</sub>: day factor, 日期因子, day in 1 ~ 31
* f<sub>wd</sub>: weekday factor, 周期（星期）因子, weekday in 1 ~ 7
* M<sub>d</sub>: day mean, 日期均值
* M<sub>wd</sub>: weekday mean, 周期（星期）均值
* V<sub>d,wd</sub>: day=d,weekday=wd的值，如V<sub>1,7</sub>表示日期为1号，且为星期日（七）的时间序列中的值。V<sub>d,wd</sub>与日期因子f<sub>d</sub>有关，也与周期因子f<sub>wd</sub>有关

根据日期进行预测的公式推导：
1. 定义：V<sub>d,wd</sub> = base * f<sub>d</sub> * f<sub>wd</sub> (这个是周期因子模型的升级版，下面的推导以这个为基础)
2. 计算：f<sub>wd</sub> = M<sub>wd</sub> / 整体均值 (这个是周期因子最基本的定义)
3. 计算：M<sub>d</sub> (求每个日期的均值)
4. 注意有这个关系存在：M<sub>d</sub> = sum(V<sub>d,wd</sub>) / 月份个数 (如计算3月到5月的M<sub>1</sub>，假设3月1号，4月1号，5月1号分别为周一，周五，周一，则M<sub>1</sub>=(V<sub>1,1</sub>+V<sub>1,5</sub>+V<sub>1,1</sub>)/3)
5. 将1中的V<sub>d,wd</sub>代入到4中，得到：

    M<sub>d</sub> = sum(base * f<sub>d</sub> * f<sub>wd</sub>) / 月份个数

    => M<sub>d</sub> = base * f<sub>d</sub> * sum(f<sub>wd</sub>) / 月份个数

    => base * f<sub>d</sub> = M<sub>d</sub> / sum(f<sub>wd</sub>) * 月份个数
6. 将上一步最后得到的式子带回到步骤1中的式子，得到：

    V<sub>d,wd</sub> = f<sub>wd</sub> * M<sub>d</sub> * 月份个数 / sum(f<sub>wd</sub>)

    PS：计算sum(f<sub>wd</sub>)时要注意，这个值和日期d是相关的，比如按上面3月到5月的例子，这里就有：
    
    sum(f<sub>wd</sub>) = 2\*f<sub>1</sub> + 0\*f<sub>2</sub> + 0\*f<sub>3</sub> + 0\*f<sub>4</sub> + 1\*f<sub>5</sub> + 0\*f<sub>6</sub> + 0\*f<sub>7</sub>

7. 由于f<sub>wd</sub>和M<sub>d</sub>都是已知的，所以可以根据这个式子来计算V<sub>d,wd</sub>了，也就是对未知的V<sub>d,wd</sub>进行预测：

    V<sub>d,wd</sub> = f<sub>wd</sub> * M<sub>d</sub> * 月份个数 / sum(f<sub>wd</sub>)

总结一下，因为搜遍各大搜索引擎都没有找到相关知识的详细介绍，所以推测周期因子并没有出现在各种教材里。周期因子只是提供了一种思想，即时间序列是有周期性的，以这种思想为指导，我们也可以灵活的设计一些自己认为合适的模型，比如大神们在这里给出的曜日(day of week)周期回归: https://raw.githubusercontent.com/YouChouNoBB/ijcai-17-top1-single-mole-solution/master/file/%E5%9F%BA%E4%BA%8E%E5%8A%A0%E6%9D%83%E5%9B%9E%E5%BD%92%E6%A8%A1%E5%9E%8B%E9%A2%84%E6%B5%8B%E5%95%86%E5%AE%B6%E6%9C%AA%E6%9D%A5%E5%AE%A2%E6%B5%81%E9%87%8F.pdf

