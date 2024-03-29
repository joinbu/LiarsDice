﻿# 单挑技巧汇总
## 辅助规则
总则：223，单骰重摇，减1变斋
- 1、骰子里面的1点是万能，可以充当任何点数。
- 2、你喊的数字必须比对方喊的数字大，不能比他小。例：A喊3个4，B只能喊3个5、3个6或者4个X、5个X等，不能喊3个2或者2

个X。
- 3、扔出豹子（即5个相同数字，例如5个X，1仍算万能）   
 规则1：仍算5个X；   
 规则2：算6个X。   
（以下讲解用规则1）   
- 4、当某人喊X个1或（2个X、N个X斋）以后，1不能当做别的数字。
- 5、当你扔出的点数5个都不一样，例如1、3、4、5、6，
规则1：重新摇骰   
规则2：见骰算骰   
规则3：什么点数均为0   
 （以下讲解用规则1，一般玩法都是规则1）

## 致胜秘籍
### 叫骰技巧：
- 1、引入坑：   
1）引下坑：叫3个5，引诱进入3个6的坑。   
2）引排坑：33366，叫3个6，引诱进入4个2，4个4，4个6的坑。   
- 2、挖坑：叫假骰，让对方进入‘必开坑’，如叫假3个5，博对方叫4个5.
- 3、车轮：11ABC,一直叫真骰，给对方开。
- 4、跳加：判断对方为真时候，可以跳加，默认对方有斋2个，飞3个。

### 开的情况：
- 1、必开情况：斋3、飞4
- 2、可开情况：对方首叫3个X飞，开飞3

### 撒谎技巧：
- 1、急转直下，如对方3个3，我方4个2
- 2、加/犹豫加1，然后直接加2

## 概率计算
### 默认概率
对方某点的个数概率分布   
<img src="https://github.com/joinbu/LiarsDice/blob/master/2.ONE%20VS%20ONE/%E7%B4%A0%E6%9D%90/ZAI_default.png">       <img src="https://github.com/joinbu/LiarsDice/blob/master/2.ONE%20VS%20ONE/%E7%B4%A0%E6%9D%90/FEI_default.png">   

### max概率
对方最多的点数个数概率分布   
<img src="https://github.com/joinbu/LiarsDice/blob/master/2.ONE%20VS%20ONE/%E7%B4%A0%E6%9D%90/ZAI_max.png">       <img src="https://github.com/joinbu/LiarsDice/blob/master/2.ONE%20VS%20ONE/%E7%B4%A0%E6%9D%90/FEI_max.png">   

## 实战分析
### 我方先叫骰
#### AAA XX
<img src="https://github.com/joinbu/LiarsDice/blob/master/material/5.png" width="40"/><img src="https://github.com/joinbu/LiarsDice/blob/master/material/5.png" width="40"/><img src="https://github.com/joinbu/LiarsDice/blob/master/material/5.png" width="40"/><img src="https://github.com/joinbu/LiarsDice/blob/master/material/2.png" width="40"/><img src="https://github.com/joinbu/LiarsDice/blob/master/material/3.png" width="40"/>   
我方叫 3个5，引诱对方叫3个6，根据‘默认概率飞图’，对方只有23.13%概率存在3个6，因此可以果断开。（为什么需要使用‘默认概率’？因为对方是被你引诱进入3个6的）。   
如果对方叫4个4，根据‘max概率飞图’，对方只有20.63%的概率存在4个4，可以果断开。（为什么使用‘max概率’？因为叫4个的话，基本可以按自己意愿随心叫）。   
####  AAA BB(AAAAB)
<img src="https://github.com/joinbu/LiarsDice/blob/master/material/6.png" width="40"/><img src="https://github.com/joinbu/LiarsDice/blob/master/material/6.png" width="40"/><img src="https://github.com/joinbu/LiarsDice/blob/master/material/6.png" width="40"/><img src="https://github.com/joinbu/LiarsDice/blob/master/material/3.png" width="40"/><img src="https://github.com/joinbu/LiarsDice/blob/master/material/3.png" width="40"/>      
<img src="https://github.com/joinbu/LiarsDice/blob/master/material/6.png" width="40"/><img src="https://github.com/joinbu/LiarsDice/blob/master/material/6.png" width="40"/><img src="https://github.com/joinbu/LiarsDice/blob/master/material/6.png" width="40"/><img src="https://github.com/joinbu/LiarsDice/blob/master/material/6.png" width="40"/><img src="https://github.com/joinbu/LiarsDice/blob/master/material/3.png" width="40"/>    
这是典型的带入坑案例，先叫3个6，将对方带入4个2，4个4，4个5的坑。
#### 11 ABC
<img src="https://github.com/joinbu/LiarsDice/blob/master/material/1.png" width="40"/><img src="https://github.com/joinbu/LiarsDice/blob/master/material/1.png" width="40"/><img src="https://github.com/joinbu/LiarsDice/blob/master/material/2.png" width="40"/><img src="https://github.com/joinbu/LiarsDice/blob/master/material/4.png" width="40"/><img src="https://github.com/joinbu/LiarsDice/blob/master/material/6.png" width="40"/>   
先叫3个2，根据对方的叫骰情况，慢慢叫3个2，3个4，4个6等，对方有1个及以上的情况为85.49%，2个及以上的情况也有52.61%，即使叫上5个，也有52.61%的胜率，而且我方经常变骰，对方会以为我方叫假骰，引诱对方开。

### 对方先叫骰
默认对方叫真骰和假骰的概率各为50%   
- 1、对方叫2个X斋，对方没有2个X的概率为50%，没有三个X的概率为88.27%，当叫到3个X斋，可开。
- 2、对方叫3个X飞，对方没有3个X的概率为61.84%，没有4个X的概率为89.40%，因此叫到3个X时候，没有更好的叫法时可开，叫到4个X时，果断开。