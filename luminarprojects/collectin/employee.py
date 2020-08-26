empl = {"eid": 100, "ename": "haritha", "desig": "developer", "salary": 25000}
for k,v in empl.items():
    print(k, " : ", v)
empl["gender"] = "female"  # to add new key value
for k, v in empl.items():
    print(k, " : ", v)
print("ename" in empl)  # to check, only return true or false
print(empl["ename"])
