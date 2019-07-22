import pandas as pd
dist = pd.read_csv('1.csv',header=0,index_col=0)

def count(df,list,what):
	c=0
	for i in range(0,pow(6,5)):
			if df.loc[i,list] == what:
				c+=1
	return c



lie='F_max_c'

x=pd.Series('')

x[0] = count(dist,lie,0)
x[1] = count(dist,lie,1)
x[2] = count(dist,lie,2)
x[3] = count(dist,lie,3)
x[4] = count(dist,lie,4)
x[5] = count(dist,lie,5)


print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])
print(x[5])
