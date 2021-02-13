
## 0. 问题
如果你是某P2P租车的技术负责人，你会如何设计个性化推荐和搜索排序

## 1. 阐述相似车型，搜索排序的设计方法
* 准备出租车辆信息，如品牌，型号，大小，颜色，车主所在地区等
* 准备基本用户特征信息，如：性别，年龄，住址
* 准备用户历史租车信息
* 对上面的特征/数据选择合适的方式计算embedding
* 用户在进行Query的时候，根据原有features+embedding features计算余弦相似度，对车辆进行排序



## 2. 可能的embedding策略

* 用户浏览并下单租车的session记录进行embedding，session概念与Airbnb项目中的session相同
* 对车辆的各种特征进行embedding
* 对租户的各种特征进行embedding




