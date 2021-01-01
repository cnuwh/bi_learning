# 知识点梳理

##	时间序列模型

* 机器学习模型：AR、MA、ARMA、ARIMA
* 神经网络模型：LSTM

|name|category|formula|
|-|-|-|
|AR|机器学习|x<sub>t</sub>=a<sub>1</sub>x<sub>t-1</sub>+...+a<sub>p</sub>x<sub>t-p</sub>+u<sub>t</sub>
|MA|机器学习|x<sub>t</sub>=u<sub>t</sub>+b<sub>1</sub>u<sub>t-1</sub>+...+b<sub>q</sub>u<sub>t-q</sub>
|ARMA|机器学习|x<sub>t</sub>=a<sub>1</sub>x<sub>t-1</sub>+...+a<sub>p</sub>x<sub>t-p</sub>+u<sub>t</sub>+b<sub>1</sub>u<sub>t-1</sub>+...+b<sub>q</sub>u<sub>t-q</sub>
|ARIMA|机器学习|ARMA + d阶差分
|LSTM|深度学习|-

u<sub>t</sub>表示t时间的白噪声，a、b为回归系数。

使用ARIMA模型进行预测，需要对差分进行还原。

## 时间序列及分解

* 趋势（trend）：时间序列在长时期内呈现出来的某种持续上升或持续下降的变动，也称长期趋势
* 季节性（seasonality）：时间序列在一年内重复出现的周期波动。销售旺季，销售淡季
* 周期性（cyclicity）：通常是由经济环境的变化引起
* 随机性（Irregular），指受偶然因素影响所形成的的不规则波动，在时间序列中无法预估

注：statsmodels中的seasonal_decompose可以将时间序列分解为trend，seasonal，residual

## LSTM
* Long Short-Term Memory，长短记忆网络
* 可以避免常规RNN的梯度消失
* 引入了三个门函数：输入门（Input Gate）、遗忘门（Forget Gate）和输出门（Output Gate）来控制输入值、记忆值和输出值
* LSTM要求的数据格式, (样本数，时间步长，特征数)


