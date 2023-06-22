import numpy as np

a=[1,2,3,4,5]

a1=np.array(a)
print(a1)
a2=np.shape(a)
print(a2)
ar=np.fromiter(a,dtype=np.int64)
print(ar)
ar1=np.arange(2,10,2)
print(ar1)
'''
import pandas as pd
data={'Name':['veer','khushal','veerkhushal'],
      'Age':[18,19,np.nan],
      'class':[10,11,12]
      }

a=pd.DataFrame(data)
'''


'''
print(a)
print(a.loc[[1,2,0]])
b=pd.DataFrame(data,index=['ok','notok','okok'])
print(b)
print(a.loc[2])

a.fillna(0)
print(a.fillna(2))
print(a.dropna())
'''
'''
t=pd.Series([12,13,12,13,14,151,611,61,51])
o=pd.Series(12)
print(t.describe())
print(t.sum())
print(t.mean())
print(t.value_counts())
print(t.loc[1])
print(t.iloc[2:5])
'''

'''
q=t.tail(4)
w=t.head()
print(w)
print(t.info())
print(w.shape)
arr=t.values
rs=arr.reshape((7,1))
print(rs)
print(t)
'''