
#-- coding: utf-8 --
import pandas as pd 	#导入数据分析库pandas
import matplotlib.pyplot as plt #导入画图库

###########设置字体，解决中文字体乱码问题###########
import matplotlib as mpl
mpl.rcParams['font.sans-serif']=['SimHei'] #指定默认字体 SimHei为黑体
mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号
###########设置字体，解决中文字体乱码问题###########


###########阶乘函数定义###########
def factorial(n):
    if n==1:
        return n
    else:
        return n * factorial(n-1)
def C(r,n):
	if r == 0:
		return 1
	elif r == n:
		return 1
	else:
		x = factorial(n)/(factorial(r)*factorial(n-r))
		return x
###########阶乘函数定义###########

#0,见骰算骰
#1,见骰算骰MAX
#2,单骰重摇
#3,单骰重摇MAX
TYPE = 0 #是否单骰重摇
PLAYERS_NUMBER = 1 #输入对面玩家数PLAYERS_NUMBER
DICE_COUNT = PLAYERS_NUMBER * 5 #计算骰子数 DICE_COUNT = PLAYERS_NUMBER *5
DF = pd.DataFrame(0.0,index =['T'], columns = range(0,DICE_COUNT+1)) #使用0.0赋值，请勿使用0，否则默认为整型，无法计算小数

#见骰算骰，斋
ZAI_JIAN = DF.copy()
ZAI_JIAN_ACCUMULATION = DF.copy()

for i in range(0,DICE_COUNT+1):
	ZAI_JIAN[i]['T'] = pow(1/6,i)*pow(5/6,DICE_COUNT-i) *C(i,DICE_COUNT)

for i in range(0,DICE_COUNT+1):
	for j in range(i,DICE_COUNT+1):
		ZAI_JIAN_ACCUMULATION[i]['T']=ZAI_JIAN[j]['T']+ZAI_JIAN_ACCUMULATION[i]['T']

#print('\n>>>>>>ZAI_JIAN\n',ZAI_JIAN)
print('\n>>>>>>ZAI_JIAN_ACCUMULATION\n',ZAI_JIAN_ACCUMULATION)
#见骰算骰，飞
FEI_JIAN = DF.copy()
FEI_JIAN_ACCUMULATION = DF.copy()

for i in range(0,DICE_COUNT+1):
	FEI_JIAN[i]['T'] = pow(1/3,i)*pow(2/3,DICE_COUNT-i) *C(i,DICE_COUNT)

for i in range(0,DICE_COUNT+1):
	for j in range(i,DICE_COUNT+1):
		FEI_JIAN_ACCUMULATION[i]['T']=FEI_JIAN[j]['T']+FEI_JIAN_ACCUMULATION[i]['T']

#print('\n>>>>>>FEI_JIAN\n',FEI_JIAN)
print('\n>>>>>>FEI_JIAN_ACCUMULATION\n',FEI_JIAN_ACCUMULATION)

#见骰算骰MAX,斋
ZAI_JIAN_MAX = DF.copy()
ZAI_JIAN_MAX_ACCUMULATION = DF.copy()

ZAI_JIAN_MAX[0]['T'] = 0
ZAI_JIAN_MAX[1]['T'] = 720/7776
ZAI_JIAN_MAX[2]['T'] = 5400/7776
ZAI_JIAN_MAX[3]['T'] = 1500/7776
ZAI_JIAN_MAX[4]['T'] = 150/7776
ZAI_JIAN_MAX[5]['T'] = 6/7776

for i in range(0,DICE_COUNT+1):
	for j in range(i,DICE_COUNT+1):
		ZAI_JIAN_MAX_ACCUMULATION[i]['T']=ZAI_JIAN_MAX[j]['T']+ZAI_JIAN_MAX_ACCUMULATION[i]['T']

#print('\n>>>>>>ZAI_JIAN_MAX\n',ZAI_JIAN_MAX)
print('\n>>>>>>ZAI_JIAN_MAX_ACCUMULATION\n',ZAI_JIAN_MAX_ACCUMULATION)

#见骰算骰MAX,飞
FEI_JIAN_MAX = DF.copy()
FEI_JIAN_MAX_ACCUMULATION = DF.copy()

FEI_JIAN_MAX[0]['T'] = 0
FEI_JIAN_MAX[1]['T'] = 120/7776
FEI_JIAN_MAX[2]['T'] = 2700/7776
FEI_JIAN_MAX[3]['T'] = 3500/7776
FEI_JIAN_MAX[4]['T'] = 1300/7776
FEI_JIAN_MAX[5]['T'] = 156/7776

for i in range(0,DICE_COUNT+1):
	for j in range(i,DICE_COUNT+1):
		FEI_JIAN_MAX_ACCUMULATION[i]['T']=FEI_JIAN_MAX[j]['T']+FEI_JIAN_MAX_ACCUMULATION[i]['T']

#print('\n>>>>>>FEI_JIAN_MAX\n',FEI_JIAN_MAX)
print('\n>>>>>>FEI_JIAN_MAX_ACCUMULATION\n',FEI_JIAN_MAX_ACCUMULATION)

#单骰重摇,斋
ZAI_TWO = DF.copy()
ZAI_TWO_ACCUMULATION = DF.copy()

ZAI_TWO[0]['T'] = 3005/7056
ZAI_TWO[1]['T'] = 2525/7056
ZAI_TWO[2]['T'] = 1250/7056
ZAI_TWO[3]['T'] = 250/7056
ZAI_TWO[4]['T'] = 25/7056
ZAI_TWO[5]['T'] = 1/7056

for i in range(0,DICE_COUNT+1):
	for j in range(i,DICE_COUNT+1):
		ZAI_TWO_ACCUMULATION[i]['T']=ZAI_TWO[j]['T']+ZAI_TWO_ACCUMULATION[i]['T']

#print('\n>>>>>>ZAI_TWO\n',ZAI_TWO)
print('\n>>>>>>ZAI_TWO_ACCUMULATION\n',ZAI_TWO_ACCUMULATION)

#单骰重摇,飞
FEI_TWO = DF.copy()
FEI_TWO_ACCUMULATION = DF.copy()

FEI_TWO[0]['T'] = 1024/7056
FEI_TWO[1]['T'] = 2320/7056
FEI_TWO[2]['T'] = 2080/7056
FEI_TWO[3]['T'] = 1280/7056
FEI_TWO[4]['T'] = 320/7056
FEI_TWO[5]['T'] = 32/7056

for i in range(0,DICE_COUNT+1):
	for j in range(i,DICE_COUNT+1):
		FEI_TWO_ACCUMULATION[i]['T']=FEI_TWO[j]['T']+FEI_TWO_ACCUMULATION[i]['T']

#print('\n>>>>>>FEI_TWO\n',FEI_TWO)
print('\n>>>>>>FEI_TWO_ACCUMULATION\n',FEI_TWO_ACCUMULATION)

#单骰重摇MAX,斋
ZAI_TWO_MAX = DF.copy()
ZAI_TWO_MAX_ACCUMULATION = DF.copy()

ZAI_TWO_MAX[0]['T'] = 0
ZAI_TWO_MAX[1]['T'] = 0
ZAI_TWO_MAX[2]['T'] = 5400/7056
ZAI_TWO_MAX[3]['T'] = 1500/7056
ZAI_TWO_MAX[4]['T'] = 150/7056
ZAI_TWO_MAX[5]['T'] = 6/7056

for i in range(0,DICE_COUNT+1):
	for j in range(i,DICE_COUNT+1):
		ZAI_TWO_MAX_ACCUMULATION[i]['T']=ZAI_TWO_MAX[j]['T']+ZAI_TWO_MAX_ACCUMULATION[i]['T']

#print('\n>>>>>>ZAI_TWO_MAX\n',ZAI_TWO_MAX)
print('\n>>>>>>ZAI_TWO_MAX_ACCUMULATION\n',ZAI_TWO_MAX_ACCUMULATION)

#单骰重摇MAX,飞
FEI_TWO_MAX = DF.copy()
FEI_TWO_MAX_ACCUMULATION = DF.copy()

FEI_TWO_MAX[0]['T'] = 0
FEI_TWO_MAX[1]['T'] = 0
for i in range(2,DICE_COUNT+1):
	FEI_TWO_MAX[i]['T'] = pow(1/3,i-2)*pow(2/3,DICE_COUNT-i) *C(i-2,DICE_COUNT-2)


for i in range(0,DICE_COUNT+1):
	for j in range(i,DICE_COUNT+1):
		FEI_TWO_MAX_ACCUMULATION[i]['T']=FEI_TWO_MAX[j]['T']+FEI_TWO_MAX_ACCUMULATION[i]['T']

#print('\n>>>>>>FEI_TWO_MAX\n',FEI_TWO_MAX)
print('\n>>>>>>FEI_TWO_MAX_ACCUMULATION\n',FEI_TWO_MAX_ACCUMULATION)

#见骰算骰
if TYPE == 0:

	plt.plot(range(0,DICE_COUNT+1),ZAI_JIAN_ACCUMULATION.loc['T',:],label = '斋',color= 'g',linestyle='-')
	plt.plot(range(0,DICE_COUNT+1),FEI_JIAN_ACCUMULATION.loc['T',:],label = '飞',color= 'b',linestyle='-')

	plt.hlines(0.5,0,PLAYERS_NUMBER*5,label = '50%线',color= 'y',linestyle = '--')
	plt.hlines(1/((PLAYERS_NUMBER+1)),0,PLAYERS_NUMBER*5,label = '均线',color= 'r',linestyle = '--')
	plt.hlines(1/((PLAYERS_NUMBER+1)*2),0,PLAYERS_NUMBER*5,label = '极限线',color= 'k',linestyle = '--')
	plt.title('见骰算骰-骰子概率表')

#见骰算骰MAX
elif TYPE == 1 and PLAYERS_NUMBER == 1:

	plt.plot(range(0,DICE_COUNT+1),ZAI_JIAN_MAX_ACCUMULATION.loc['T',:],label = '斋',color= 'g',linestyle='-')
	plt.plot(range(0,DICE_COUNT+1),FEI_JIAN_MAX_ACCUMULATION.loc['T',:],label = '飞',color= 'b',linestyle='-')
	
	plt.hlines(0.5,0,PLAYERS_NUMBER*5,label = '50%线',color= 'y',linestyle = '--')
	plt.hlines(1/((PLAYERS_NUMBER+1)),0,PLAYERS_NUMBER*5,label = '均线',color= 'r',linestyle = '--')
	plt.hlines(1/((PLAYERS_NUMBER+1)*2),0,PLAYERS_NUMBER*5,label = '极线',color= 'k',linestyle = '--')
	plt.title('见骰算骰MAX-骰子概率表')

#单骰重摇
elif TYPE == 2 and PLAYERS_NUMBER == 1:

	plt.plot(range(0,DICE_COUNT+1),ZAI_TWO_ACCUMULATION.loc['T',:],label = '斋',color= 'g',linestyle='-')
	plt.plot(range(0,DICE_COUNT+1),FEI_TWO_ACCUMULATION.loc['T',:],label = '飞',color= 'b',linestyle='-')
	
	plt.hlines(0.5,0,PLAYERS_NUMBER*5,label = '50%线',color= 'y',linestyle = '--')
	plt.hlines(1/((PLAYERS_NUMBER+1)),0,PLAYERS_NUMBER*5,label = '均线',color= 'r',linestyle = '--')
	plt.hlines(1/((PLAYERS_NUMBER+1)*2),0,PLAYERS_NUMBER*5,label = '极线',color= 'k',linestyle = '--')
	plt.title('单骰重摇-骰子概率表')

#单骰重摇MAX
elif TYPE == 3:
	if PLAYERS_NUMBER == 1:
		plt.plot(range(0,DICE_COUNT+1),ZAI_TWO_MAX_ACCUMULATION.loc['T',:],label = '斋',color= 'g',linestyle='-')
	plt.plot(range(0,DICE_COUNT+1),FEI_TWO_MAX_ACCUMULATION.loc['T',:],label = '飞',color= 'b',linestyle='-')
	
	plt.hlines(0.5,0,PLAYERS_NUMBER*5,label = '50%线',color= 'y',linestyle = '--')
	plt.hlines(1/((PLAYERS_NUMBER+1)),0,PLAYERS_NUMBER*5,label = '均线',color= 'r',linestyle = '--')
	plt.hlines(1/((PLAYERS_NUMBER+1)*2),0,PLAYERS_NUMBER*5,label = '极线',color= 'k',linestyle = '--')
	plt.title('单骰重摇MAX-骰子概率表')
else:
	exit()

plt.xlabel('个数')
plt.ylabel('概率')

plt.legend()	#显示图例
plt.show()