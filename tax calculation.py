income=int(input("Enter Salary :"))
if income <= 250000:  
    tax = 0
elif income <= 500000: 
    tax = (income - 250000) * 0.05
    print(income-tax)
elif income <= 750000: 
    tax = (income - 500000) * 0.10 + 12500
    print(income-tax)
elif income <= 1000000: 
    tax = (income - 750000) * 0.15 + 37500 
    print(income-tax)
elif income <= 1250000: 
    tax = (income - 1000000) * 0.20 + 75000 
    print(income-tax)
elif income <= 1500000: 
    tax = (income - 1250000) * 0.25 + 125000 
    print(income-tax)
else:
    tax = (income - 1500000) * 0.30 + 187500
print("you own", tax, "Rupees in tax!")
