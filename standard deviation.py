#Standard Deviation

import math
z=[1,2,3,4,5,6,7]
x=[18,15,16,17,16,25,19]
d=[]
d2=[]
x2=[]
n=0
totalx=0
totald2=0
totalx2=0
for i in range(len(x)):
    n=n+1
    totalx=totalx+x[i]
    d.append(x[i]-x[i])
    d2.append(d[i]*d[i])
    totald2=totald2+d2[i]
    x2.append(x[i]*x[i])
    totalx2=totalx2+x2[i]
print(totalx2)
ans=math.sqrt((totalx2/n)-(totalx/n)**2)
print(ans)