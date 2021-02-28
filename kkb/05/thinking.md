
### Thinking1 电商定向广告和搜索广告有怎样的区别，算法模型是否有差别

* 用户没有很明显的意图（主动的Query查询）
* 用户来到淘宝之前，自己也没有特别明确的目标（利用以往的历史行为 => item推荐）
* p(y=1 | ad, context, user)
  * ad 表示广告候选集
  * user 表示用户特征，年龄、性别
  * context 表示上下文场景，设备，时间

### Thinking2 定向广告都有哪些常见的使用模型，包括Attention机制模型

* LR模型（线性模型）
* MLR模型（非线性模型）
* DNN模型（深度学习）
* DIN(Deep Interest Network)
* DIEN(Deep Interest Evolution Network)
* DSIN(Deep Session Interest Network)

### Thinking3 DIN中的Attention机制思想和原理是怎样的

* 在对用户行为的embedding计算上引入了attention network (也称为Activation Unit) 
* 把用户历史行为特征进行embedding操作，视为对用户兴趣的表示，之后通过Attention Unit，对每个兴趣表示赋予不同的权值
* Attention Weight是由用户历史行为和候选广告进行匹配计算得到的
* 通过Attention Weight保留用户的兴趣强度
比如，用户的点击序列中90%是衣服，10%是电子产品，有两个候选ad（T恤和手机），T恤的候选ad 激活属于衣服和衣服的大部分历史行为会比手机获得更大的兴趣强度


### Thinking4 DIEN相比于DIN有哪些创新

DIN的不足：
* 利用用户行为序列特征，直接把用户历史行为当做兴趣
* 直接用行为表示兴趣可能存在问题。因为行为是序列化产生的，行为之间存在依赖关系，比如当前时刻的兴趣往往直接导致了下一行为的发生
* 用户的兴趣是不断进化的，而DIN抽取的用户兴趣之间是独立无关联的，没有捕获到兴趣的动态进化性，比如用户对衣服的喜好，会随季节、时尚风潮以及个人品味的变化而变化，呈现一种连续的变迁趋势。

DIEN的创新：
* 通过引入序列模型 AUGRU 模拟了用户兴趣进化的过程
在 Embedding layer 和 Concatenate layer 之间加入了生成兴趣的 Interest Extractor Layer 和模拟兴趣演化的 Interest Evolving layer
* Interest Extractor Layer 使用了GRU的结构抽取了每一个时间片内用户的兴趣
* Interest Evolving layer 利用序列模型 AUGRU 的结构将不同时间的用户兴趣串联起来，形成兴趣进化的链条
* 最终把当前时刻的“兴趣向量”输入上层的多层全连接网络，与其他特征一起进行最终的 CTR 预估


### Thinking5 DSIN关于Session的洞察是怎样的，如何对Session兴趣进行表达

用户行为洞察：
* Sequence视角，同样可以看到user interest的变化
* Session视角，每个Session中的行为是相近的，而在不同会话之间差别是很大的（类似聚类）
* Session的划分和airbnb一样，即将用户的点击行为按照时间排序，前后的时间间隔大于30min，算成另一个session


### Thinking6 如果你来设计淘宝定向广告，会有哪些future work（即下一个阶段的idea）

加入兴趣推测的逻辑。
用户历史的session记录中，只包含了用户兴趣的一小部分，可以根据用户的历史session，对用户其他的兴趣进行推测，从而推荐相关的广告。
