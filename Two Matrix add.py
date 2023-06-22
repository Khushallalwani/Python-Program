x=[[1,2,3],
   [4,5,6],
   [7,8,9]]

y=[[11,12,13],
   [14,15,16],
   [17,18,19]]

z=[[0,0,0],
   [0,0,0],
   [0,0,0]]
'''
for i in range(len(x)):
    for j in range(len(y[0])):
       z[i][j]=x[i][j]+y[i][j] 
for r in z:
    print(r)
'''

'''
for i in range(len(x)):
    for j in range(len(y[0])):
        z[i][j]=+y[i][j]-x[i][j]
for r in z:
    print(r)
'''

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            z[i][j]=z[i][j]+x[i][j]*y[i][j]
for r in z:
    print(r)
