
# 心得笔记


AlphaGo Zero：

* Mastering the game of Go without human knowledge，2017
https://www.gwern.net/docs/rl/2017-silver.pdf
* 使用一个参数为θ的深度神经网络f_θ(s_t)，将棋盘表示和历史记录作为输入，输出落子概率和价值 (p,v) = f_θ(s)
* 落子概率向量p代表选择每个落子动作a（包括放弃行棋）的概率p_a = Pr(a|s)
* 价值v是标量评估，估计当前玩家在棋局状态为 s 时获胜的可能性
* AlphaGo Zero神经网络将策略网络和价值网络合并成一个单一的体系结构，其中神经网络由13层的卷积神经网络组成
* 对于每个棋局s，通过神经网络f_θ(s)的指导来执行MCTS搜索，MCTS搜索输出每次落子的概率分布π。
* 经过搜索后的落子概率p 通常比神经网络f_θ(s)输出的落子概率p更强 => 将MCTS看作是一个强大的策略改进算法
