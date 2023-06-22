x=int(input("Enter first age :"))
y=int(input("Enter second age :"))
z=int(input("Enter third age :"))

if x>=y and x>=z:
  print("Oldest is x",x)
elif y>=x and y>=z:
  print("Oldest is y",y)
elif z>=x and z>=y:
  print("Oldest is z",z)
else:
  print("All are equal")	
