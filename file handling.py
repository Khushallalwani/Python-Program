file=open('veer.txt','r')
file.close()
file=open('veer.txt','w+')
file.write("VEERkhushal lalwani")
file.write("hello")
file.close()
with open('veer.txt','w+') as f:
    f.write("HELLO WORLD")