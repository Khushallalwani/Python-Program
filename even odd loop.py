a=[1,2,3,4,5,7,8,9,10]
even=0
odd=0
z=0
'''
for i in range(0,9,1):
    if a[i]%2==0:
        even=even+1
        print("Even Number")
    else:
        odd=odd+1
        print("odd Number")
        '''
for i in a:
    if i%2==0:
        even=even+1
        print("Even Number",i)
    else:
        odd=odd+1
        print("odd Number",i)     
