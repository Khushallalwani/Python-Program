a=[1,2,3,4,5]
n=len(a)
for i in range(0,int(n/2),1):
    temp=a[i]
    a[i]=a[n-1]
    a[n-1]=temp
    n=n-1
print(a)