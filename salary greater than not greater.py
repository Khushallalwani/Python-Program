s=int(input("Enter Sales :"))
if s>=100000:
    basic=4000
    hr=4000*20/100
    da=4000*110/100
    con=500
    incen=s*10/100
    bonus=1000
    a=hr+da+con+incen+bonus
    print(a)
else:
    basic=4000
    hr=4000*20/100
    da=4000*110/100
    con=500
    incen=s*4/100
    bonus=500
    a=hr+da+con+incen+bonus
    print(a)