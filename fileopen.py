f=open("day1.txt","r")

st=f.read()
print(len(st))
for i in range(len(st)):
    print(st[i],i)
f.close()

