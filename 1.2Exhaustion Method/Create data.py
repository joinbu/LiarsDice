import pandas as pd

dist = pd.DataFrame(0.0,index =['T'],columns = ['一','二','三','四','五'])
# dist = pd.DataFrame(0.0,index =['T'], columns = range(0,1))

dist['三'][0] = 10 
print(dist)

dist.to_csv('1.csv')