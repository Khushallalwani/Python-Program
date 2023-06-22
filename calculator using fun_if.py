def add(num,num1):
    return num+num1
def subtract(num,num1):
    return num-num1
def multiply(num,num1):
    return num*num1
def divide(num,num1):
    return num/num1

print("Please Select Operation -\n" \
      "1. Add\n"\
      "2. Subtract\n"\
      "3. Multiply\n"\
      "4. Divide\n")
select=int(input("Select Operation form 1,2,3,4 :"))
num=int(input("Enter a Number :"))
num1=int(input("Enter b Number :"))

if select==1:
    print(add(num,num1))
elif select==2:
    print(subtract(num,num1))
elif select==3:
    print(multiply(num,num1))
elif select==4:
    print(divide(num,num1))
else:
    print("Invalid Choice")





