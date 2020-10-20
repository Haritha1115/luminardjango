# Date,Name of State ,Latitude,Longitude,Total Confirmed cases,Death,Discharged,New cases,New deaths,New recovered
f = open("complete.csv","r")
dict = {}
for data in f:
    data = data.rstrip("\n").split(",")
    name = data[1]
    ccase = data[4]
    if name not in dict:
        dict[name] = ccase
    else:
        dict[name] = ccase
print(dict)
maxlst = max(dict,key =dict.get)
print("state with highest confirmed case :",maxlst)

