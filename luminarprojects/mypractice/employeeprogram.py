class emp:
    def setvalues(self, id, name, desig, salary):
        self.eid = id
        self.ename = name
        self.edesig = desig
        self.sal = salary

    def printinfo(self):
        print("ID :", self.eid)
        print("NAME :", self.ename)
        print("DESIGNATION :", self.edesig)
        print("SALARY :", self.sal)


lst = []
obj = emp()
i = 0
num = int(input(" enter number of information want record :"))

while num > 0:
    id = input("enter the id :")
    name = input("enter the name :")
    desig = input(" enter the designation :")
    salary = int(input("enter the salary :"))
    lst.append(obj.setvalues(id, name, desig, salary))
    num -= 1
    #i += 1
# # for i in range(0,num):
# #     obj[i].printinfo()
# #     i += 1
# for items in lst :
#     print(items)
