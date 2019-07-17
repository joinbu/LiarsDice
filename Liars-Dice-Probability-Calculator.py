
import pandas as pd
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



#输入玩家数PLAYERS_NUMBER
PLAYERS_NUMBER = 2

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

print('\n>>>>>>ZAI_JIAN\n',ZAI_JIAN)
print('\n>>>>>>ZAI_JIAN_ACCUMULATION\n',ZAI_JIAN_ACCUMULATION)

#飞，见骰算骰
FEI_JIAN = DF.copy()
FEI_JIAN_ACCUMULATION = DF.copy()

for i in range(0,DICE_COUNT+1):
	FEI_JIAN[i]['T'] = pow(1/3,i)*pow(2/3,DICE_COUNT-i) *C(i,DICE_COUNT)

for i in range(0,DICE_COUNT+1):
	for j in range(i,DICE_COUNT+1):
		FEI_JIAN_ACCUMULATION[i]['T']=FEI_JIAN[j]['T']+FEI_JIAN_ACCUMULATION[i]['T']

print('\n>>>>>>FEI_JIAN\n',FEI_JIAN)
print('\n>>>>>>FEI_JIAN_ACCUMULATION\n',FEI_JIAN_ACCUMULATION)



#飞，两个人玩，单骰重新摇
FEI_TWO = pd.DataFrame(0.0,index =['T'], columns = range(0,5+1))
FEI_TWO_ACCUMULATION = FEI_TWO.copy()


FEI_TWO[0]['T'] = 0
FEI_TWO[1]['T'] = 0
FEI_TWO[2]['T'] = 64/216
FEI_TWO[3]['T'] = 1/3*pow(2/3,2)*3
FEI_TWO[4]['T'] = pow(1/3,2)*2/3*3
FEI_TWO[5]['T'] = pow(1/3,3)


for i in range(0,5+1):
	for j in range(i,5+1):
		FEI_TWO_ACCUMULATION[i]['T']=FEI_TWO[j]['T']+FEI_TWO_ACCUMULATION[i]['T']

print('\n>>>>>>FEI_TWO\n',FEI_TWO)
print('\n>>>>>>FEI_TWO_ACCUMULATION\n',FEI_TWO_ACCUMULATION)

