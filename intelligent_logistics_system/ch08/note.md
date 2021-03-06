# 启发式算法：
* 相对于最优化算法提出的，一个问题的最优算法求得该问题每个实例的最优解
* 启发式算法可以这样定义：一个基于直观或经验构造的算法，在可接受的花费（指计算时间和空间）下给出待解决组合优化问题每一个实例的一个可行解，该可行解与最优解的偏离程度一般不能被预计
* 一般用于解决NP-hard问题，其中NP是指非确定性多项式
* 常用的算法有：模拟退火算法（SA）、遗传算法（GA）、蚁群算法（ACO）、人工神经网络（ANN）
* 对于NP Hard问题，可行时间内在各空间中找到全局最优解的可能性很小，需要使用近似算法（Approximate Method）在有限时间内寻找一个近似最优解
* 近似方法分成：近似算法 和 启发式算法
* 近似算法，可以得到一个有质量保证的解，而启发式算法可以在可行时间内找到一个相对比较好的解，但对解的质量没有保证

# 遗传算法：
* 通过模拟自然进化过程（达尔文生物进化论）搜索最优解的方法，遗传操作包括：选择、交叉和变异
* 算法核心：参数编码、初始群体的设定、适应度函数、遗传操作设计、控制参数设定
* 以一种群体中的所有个体为对象，利用随机化技术指导对一个被编码的参数空间进行高效搜索

# 遗传算法特点：
* 直接对结构对象进行操作，不存在求导和函数连续性的限定
* 具有内在的隐并行性和更好的全局寻优能力
* 采用概率化的寻优方法，不需要确定的规则就能自动获取和指导优化的搜索空间，自适应地调整搜索方向

# 遗传算法步骤：
* 在既定的区间内找出函数的最大值
* 相当于袋鼠蹦跳的过程，需要设计一种编码方式，二进制编码法1110001010111
* Step1，随机初始化一个种群，即第一批袋鼠
* Step2，通过解码过程，得到袋鼠的位置，用适应性函数对每一个基因个体作评估（适应度越高越好）
* Step3，用选择函数按照某个规则择优选择（每隔一段时间，kill适应度差的袋鼠，保证总体数目持平）
* Step4，让个体基因变异，产生子代
