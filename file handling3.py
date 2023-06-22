f=open('khushal.txt','w')
f.write('khushal')
f.close()

f=open("khushal.txt",'w+')
print(f.read())
f.write('veerkhushal')
f.close()
