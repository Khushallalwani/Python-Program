days=int(input("Enter Days :"))
year=int(days/365)
weeks=(days%365)/7
days=days-((year*365)+(weeks*7))
print(int(days))
print(int(weeks))
print(int(year))