a=[1,2,3,4,5]
s=len(a)
n=a[0]
for i in range(s):
    if n<a[i]:
        n=a[i]
    else:
        n=n
print(n)        
        