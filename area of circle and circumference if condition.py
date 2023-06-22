r=int(input("Enter Radius :"))
if r>=0: 
    areaofcircle=(3.14)*r*r
    circumferenceofcircle=2*(3.14)*r
    print(areaofcircle)
    print(circumferenceofcircle)
else:
    print("choice greater than zero")