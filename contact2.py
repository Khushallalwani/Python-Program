def menu():
    print("-----------------------------------------------------------------")
    print("**********************Khushal Contact Book***********************")
    print("-----------------------------------------------------------------")
    print("1. Add a new Contact")
    print("2. Display all Contacts")
    print("3. Search for a Contact")
    print("4. Delete contact")
    print("5. Exit PhoneBook")
    x=int(input("Enter Any choice :"))
    print(x)
def delete_contact():
   return pb.clear()  

ch=1    
pb="hlo"
while ch in(1,2,3,4,5):
    ch=menu()
    if ch==1:
        pb.add_contact()
    elif ch==2:
        
    elif ch==3:
       
    elif ch==4:
        pb.delete_contact()
    elif ch==5:
        