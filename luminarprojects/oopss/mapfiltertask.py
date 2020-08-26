import functools


class employee:
    def __init__(self, eid, name, desn, salary):
        self.eid = eid
        self.ename = name
        self.des = desn
        self.sal = salary

    def printval(self):
        print("employee id :", self.eid)
        print("employee name :", self.ename)
        print("employee designation :", self.des)
        print("employee salary :", self.sal)

    def __str__(self):
        return self.ename


f = open("edetails", "r")
lst = []
for details in f:
    det = details.rstrip("\n").split(",")
    eid = det[0]
    name = det[1]
    desn = det[2]
    salary = det[3]
    obj = employee(eid, name, desn, salary)
    obj.printval()
    lst.append(obj)

out = list(map(lambda obj: obj.ename.upper(), lst))
out1 = list(filter(lambda obj: int(obj.sal) > 25000, lst))
out2 = list(map(lambda obj: int(obj.sal) + 5000, lst))
print("names in capital :", out)
# print("names with sal>25000 :", out1)  this alone will show m/o address
print("person with salary >25000")
for i in out1:  # for filter we use for loop for output
    print(i)
print("salary with increment :", out2)
mx = functools.reduce(lambda obj1, obj2: obj1 if obj1 > obj2 else obj2, list(map(lambda obj0: obj0.sal, lst)))
print("max salary: ", mx)  # check this above line

# salaries = list(map(lambda obj:obj.sal ,lst))
# print(salaries)
# mx = functools.reduce(lambda obj1,obj2: obj1 if obj1 > obj2 else obj2, salaries) #line 45+46+47 = 43
# print(mx)
# mx = max(salaries) #by using salaries we can use max fun but not with objects
# print(mx)
