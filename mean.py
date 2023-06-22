x=[105,115,125,135,145,155,165,175]
f=[4,6,20,32,33,17,8,2]
a=135
n=0
dx=[0,0,0,0,0,0,0,0]
fdx=[0,0,0,0,0,0,0,0]
d_x=[0,0,0,0,0,0,0,0]
total=0
for i in range(len(x)):
    dx[i]=x[i]-a  
print("dx :",dx)

for j in range(len(f)):
    n=n+f[j]    
print("N :",n)    
i1=x[1]-x[0]
for k in range(len(dx)):
    d_x[k]=int(dx[k]/i1)
print("d'x :",d_x)
for t in range(len(d_x)):
    fdx[t]=d_x[t]*f[t]
print("fd'x :",fdx)
for p in range(len(fdx)):
    total=total+fdx[p]
print("Total :",total)
ans=a+total/n*i1
print(ans)