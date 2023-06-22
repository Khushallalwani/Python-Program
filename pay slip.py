employee_name=input("Enter Name:")
employee_id=int(input("Enter Employee id:"))
designation=input("Enter Designation:")
department=input("Enter Department:")
doj=input("Enter DOJ:")
uan=int(input("Enter UAN:"))
pf_no=int(input("Enter PF No:"))
esi_no=int(input("Enter ESI No:"))
bank_name=input("Enter Bank Name:")
bank_account_no=int(input("Enter Bank A/C No:"))


total_working_days=int(input("Enter Total Working Days:"))
paid_days=int(input("Enter Paid Days:"))
lop_days=int(input("Enter LOP days:"))
leaves_taken=int(input("Enter Leaves Taken:"))


basic_wage=float(input("Enter Basic Wage:"))
hra=float(input("Enter HRA:"))
conveyance_allowances=float(input("Enter Conveyance Allowances:"))
medical_allowances=float(input("Enter medical_Allowances:"))
other_allowances=float(input("Enter Other_Allowances:"))

total_earnings=basic_wage+hra+conveyance_allowances+medical_allowances+other_allowances


basic_salary=int(input("Enter Basic Salary:"))
epf=12/basic_salary*100
professional_tax=15/basic_wage*100
tds=10/basic_salary*100
esi=0.75/basic_wage*100

total_deduction=epf+professional_tax+tds+esi

net_salary=total_earnings-total_deduction

print("|--------------------------------------------------------------------|")
print("|                       COMPANY NAME                     ")
print("---------------------------------------------------------------------|")
print("|                  Address of the company           ")
print("---------------------------------------------------------------------|")
print("|                  Pay Slip For July 2022           ")
print("---------------------------------------------------------------------|")
print(" Name of the Employee",employee_name,"         UAN   ",uan)
print(" Employee ID  ",employee_id,"               PF No  ",pf_no)
print(" Designation  ",designation,"        ESI NO  ",esi_no)
print(" Department  ",department,"        Bank Name  ",bank_name)
print(" DOJ",doj)









