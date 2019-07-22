import pandas as pd

#导入数据，并制定行索引和列索引
dist = pd.read_csv('1.csv',header=0,index_col=0)

# #CY：是否重摇
# dist['CY'] = 1

# #判断是否单骰
# def not_same(df,h):
# 	a1 = df.loc[h,'1']
# 	a2 = df.loc[h,'2']
# 	a3 = df.loc[h,'3']
# 	a4 = df.loc[h,'4']
# 	a5 = df.loc[h,'5']
# 	if a1 != a2 and a1 != a3 and a1 != a4 and a1 != a5 and a2 != a3 and a2 != a4 and a2 != a5 and a3 != a4  and a3 != a5 and a4 != a5:
# 		return True
# 	else:
# 		return False

# #判断单骰并写入
# for i in range(0,pow(6,5)):
# 	if not_same(dist,i):
# 		dist.loc[i,'CY'] = 10

# dist['Z_count_1'] = 0
# dist['Z_count_2'] = 0
# dist['Z_count_3'] = 0
# dist['Z_count_4'] = 0
# dist['Z_count_5'] = 0
# dist['Z_count_6'] = 0

# #计算各点数个数
# def count_zai(df,h):
# 	a=[0,0,0,0,0,0]
# 	a[1] = df.loc[h,'1']
# 	a[2] = df.loc[h,'2']
# 	a[3] = df.loc[h,'3']
# 	a[4] = df.loc[h,'4']
# 	a[5] = df.loc[h,'5']
# 	c=[0,0,0,0,0,0,0]
# 	c[1]=0
# 	c[2]=0
# 	c[3]=0
# 	c[4]=0
# 	c[5]=0
# 	c[6]=0

# 	for i in range(1,6):
# 		for j in range(1,7):
# 			if a[i] == j:
# 				c[j]+=1
# 	return c[1],c[2],c[3],c[4],c[5],c[6]

# #计算各点（ZAI）个数并写入
# for i in range(0,pow(6,5)):
# 	dist.loc[i,'Z_count_1'],dist.loc[i,'Z_count_2'],dist.loc[i,'Z_count_3'],dist.loc[i,'Z_count_4'],dist.loc[i,'Z_count_5'],dist.loc[i,'Z_count_6']= count_zai(dist,i)


dist['F_count_1'] = 0
dist['F_count_2'] = 0
dist['F_count_3'] = 0
dist['F_count_4'] = 0
dist['F_count_5'] = 0
dist['F_count_6'] = 0

#计算各点飞的个数
def count_fei(df,h):
	a=[0,0,0,0,0,0]
	a[1] = df.loc[h,'1']
	a[2] = df.loc[h,'2']
	a[3] = df.loc[h,'3']
	a[4] = df.loc[h,'4']
	a[5] = df.loc[h,'5']
	c=[0,0,0,0,0,0,0]
	c[1]=0
	c[2]=0
	c[3]=0
	c[4]=0
	c[5]=0
	c[6]=0

	for i in range(1,6):
		for j in range(1,7):
			if a[i] == j:
				c[j]+=1

	c[2] = c[1] + c[2]
	c[3] = c[1] + c[3]
	c[4] = c[1] + c[4]
	c[5] = c[1] + c[5]
	c[6] = c[1] + c[6]

	return c[1],c[2],c[3],c[4],c[5],c[6]

#计算各点（FEI）个数并写入
for i in range(0,pow(6,5)):
	dist.loc[i,'F_count_1'],dist.loc[i,'F_count_2'],dist.loc[i,'F_count_3'],dist.loc[i,'F_count_4'],dist.loc[i,'F_count_5'],dist.loc[i,'F_count_6']= count_fei(dist,i)
	print(i)
	print(count_fei(dist,i))

dist.to_csv('1.csv')









