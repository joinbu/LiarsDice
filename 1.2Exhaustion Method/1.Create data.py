import pandas as pd

dist = pd.DataFrame(0.0,index =range(0,pow(6,5)),columns =range(1,6))
#dist = pd.DataFrame(0.0,index =['T'],columns = ['一','二','三','四','五'])

h = 0
l=0
for i1 in range(1,7):
	for i2 in range(1,7):
		for i3 in range(1,7):
			for i4 in range(1,7):
				for i5 in range(1,7):
					dist.iloc[h,l] = i1
					dist.iloc[h,l+1] = i2
					dist.iloc[h,l+2] = i3
					dist.iloc[h,l+3] = i4
					dist.iloc[h,l+4] = i5
					h=h+1
					print(h)

print(dist)

dist.to_csv('1.csv')