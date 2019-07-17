
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


#输入对面玩家数PLAYERS_NUMBER
PLAYERS_NUMBER = 4

#是否单骰重摇
CHONG = 1

#计算骰子数 DICE_COUNT = PLAYERS_NUMBER *5
DICE_COUNT = PLAYERS_NUMBER * 5

#生成DataFrame，ZAI_JIAN 与 FEI，

DF = pd.DataFrame(0.0,index =['T'], columns = range(0,DICE_COUNT+1)) #使用0.0赋值，请勿使用0，否则默认为整型，无法计算小数

#斋，见骰算骰
ZAI_JIAN = DF.copy()
ZAI_JIAN_ACCUMULATION = DF.copy()

for i in range(0,DICE_COUNT+1):
	ZAI_JIAN[i]['T'] = pow(1/6,i)*pow(5/6,DICE_COUNT-i) *C(i,DICE_COUNT)

for i in range(0,DICE_COUNT+1):
	for j in range(i,DICE_COUNT+1):
		ZAI_JIAN_ACCUMULATION[i]['T']=ZAI_JIAN[j]['T']+ZAI_JIAN_ACCUMULATION[i]['T']

#print('\n>>>>>>ZAI_JIAN\n',ZAI_JIAN)
print('\n>>>>>>ZAI_JIAN_ACCUMULATION\n',ZAI_JIAN_ACCUMULATION)

#飞，见骰算骰
FEI_JIAN = DF.copy()
FEI_JIAN_ACCUMULATION = DF.copy()

for i in range(0,DICE_COUNT+1):
	FEI_JIAN[i]['T'] = pow(1/3,i)*pow(2/3,DICE_COUNT-i) *C(i,DICE_COUNT)

for i in range(0,DICE_COUNT+1):
	for j in range(i,DICE_COUNT+1):
		FEI_JIAN_ACCUMULATION[i]['T']=FEI_JIAN[j]['T']+FEI_JIAN_ACCUMULATION[i]['T']

#print('\n>>>>>>FEI_JIAN\n',FEI_JIAN)
print('\n>>>>>>FEI_JIAN_ACCUMULATION\n',FEI_JIAN_ACCUMULATION)

#斋，单骰重摇
ZAI_TWO = DF.copy()
ZAI_TWO_ACCUMULATION = DF.copy()

ZAI_TWO[0]['T'] = 0
ZAI_TWO[1]['T'] = 0
for i in range(2,DICE_COUNT+1):
	ZAI_TWO[i]['T'] = pow(1/6,i-2)*pow(5/6,DICE_COUNT-i) *C(i-2,DICE_COUNT-2)


for i in range(0,DICE_COUNT+1):
	for j in range(i,DICE_COUNT+1):
		ZAI_TWO_ACCUMULATION[i]['T']=ZAI_TWO[j]['T']+ZAI_TWO_ACCUMULATION[i]['T']

#print('\n>>>>>>ZAI_TWO\n',ZAI_TWO)
print('\n>>>>>>ZAI_TWO_ACCUMULATION\n',ZAI_TWO_ACCUMULATION)




#飞，单骰重摇
FEI_TWO = DF.copy()
FEI_TWO_ACCUMULATION = DF.copy()

FEI_TWO[0]['T'] = 0
FEI_TWO[1]['T'] = 0
for i in range(2,DICE_COUNT+1):
	FEI_TWO[i]['T'] = pow(1/3,i-2)*pow(2/3,DICE_COUNT-i) *C(i-2,DICE_COUNT-2)


for i in range(0,DICE_COUNT+1):
	for j in range(i,DICE_COUNT+1):
		FEI_TWO_ACCUMULATION[i]['T']=FEI_TWO[j]['T']+FEI_TWO_ACCUMULATION[i]['T']

#print('\n>>>>>>FEI_TWO\n',FEI_TWO)
print('\n>>>>>>FEI_TWO_ACCUMULATION\n',FEI_TWO_ACCUMULATION)


#见骰算骰
if CHONG != 1:

	plt.plot(range(0,DICE_COUNT+1),ZAI_JIAN_ACCUMULATION.loc['T',:],label = '斋',color= 'g',linestyle='-')
	plt.plot(range(0,DICE_COUNT+1),FEI_JIAN_ACCUMULATION.loc['T',:],label = '飞',color= 'b',linestyle='-')

	plt.hlines(0.5,0,PLAYERS_NUMBER*5,label = '50%线',color= 'y',linestyle = '--')
	plt.hlines(1/((PLAYERS_NUMBER+1)),0,PLAYERS_NUMBER*5,label = '均线',color= 'r',linestyle = '--')
	plt.hlines(1/((PLAYERS_NUMBER+1)*2),0,PLAYERS_NUMBER*5,label = '极限线',color= 'k',linestyle = '--')
	plt.title('见骰算骰-骰子概率表')

#单骰重摇
if CHONG == 1:

	plt.plot(range(0,DICE_COUNT+1),ZAI_TWO_ACCUMULATION.loc['T',:],label = '斋',color= 'g',linestyle='-')
	plt.plot(range(0,DICE_COUNT+1),FEI_TWO_ACCUMULATION.loc['T',:],label = '飞',color= 'b',linestyle='-')
	
	plt.hlines(0.5,0,PLAYERS_NUMBER*5,label = '50%线',color= 'y',linestyle = '--')
	plt.hlines(1/((PLAYERS_NUMBER+1)),0,PLAYERS_NUMBER*5,label = '均线',color= 'r',linestyle = '--')
	plt.hlines(1/((PLAYERS_NUMBER+1)*2),0,PLAYERS_NUMBER*5,label = '极线',color= 'k',linestyle = '--')
	plt.title('单骰重摇-骰子概率表')

plt.xlabel('个数')
plt.ylabel('概率')

plt.legend()	#显示图例
plt.show()