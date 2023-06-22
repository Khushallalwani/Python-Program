'''
num1=15
num2=12
import operator
su=operator.add(num1, num2)
print(su)


a='1101'
b='100'
sum=bin(int(a,2)+int(b,2))
print(sum)



def maximum(a,b):
    if a>=b:
        return a
    else:
        return b

print(maximum(10,20))



aa=25
bb=40
maximum=max(aa, bb)
print(maximum)

'''



'''
a=2
b=4
print(a if a>=b else b)




a=2
b=4
maximum=lambda a,b:a if a>b else b
print(f'{maximum(a,b)} is a maximum number')



'''




'''
a=2
b=4
x=[a,b]
x.sort()
print(x[-1])

'''


'''
def simple_interest(p,t,r):
    print("The Principal is",p)
    print("The time period is",t)
    print("The rate of Interest is",r)
    si=(p*t*r)/100
    print(si)
    return si
simple_interest(8,6,8)


'''



'''

def compound_interest(principal,rate,time):
    amount=principal*(pow((1+rate/100),time))
    ci=amount-principal
    print(ci)

compound_interest(10000, 10.25,5)


'''




'''
def findarea(r):
    pi=3.142
    return pi*(r*r)

print(findarea(5))

'''


'''
import math
def area(r):
    area=math.pi*pow(r,2)
    
    return area
print(area(4))

'''


'''
num1=6.3
sum=num+num1
print("The sum of {0} and {1} is {2}".format(num,num1,sum))
'''

'''

a=5
b=6
c=7
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))
print(area)
'''

'''
import cmath

a=1
b=5
c=6
d=(b**2)-(4*a*c)
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)

print(sol1,sol2)

'''