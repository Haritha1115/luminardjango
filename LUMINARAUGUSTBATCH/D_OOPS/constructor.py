# class employee:
#     cname = "luminar"
#     def setEmp(self,id,ename,desig,salary):
#         self.id = id
#         self.desig = desig
#         self.salary = salary
#         self.ename = ename
#
#     def printEmp(self):
#         print(" company :", employee.cname)
#         print(" id :",self.id)
#         print(" name :",self.ename)
#         print("designation :",self.desig)
#         print(" salary :",self.salary)
#
# emp = employee()
# emp.setEmp(101,"hari","ceo",45600)
# emp.printEmp()

# constructor is used to intialise the instance varible ...as setemp is doing'
# it is always __init__()
# constructor is automatically invoke(called) at the time of object creation

# here replacing aboove using cinstructor
# class employee:
#     cname = "luminar"
#     def __init__(self,id,ename,desig,salary):  # constructror
#         self.id = id
#         self.desig = desig
#         self.salary = salary
#         self.ename = ename
#
#     def printEmp(self):
#         print(" company :", employee.cname)
#         print(" id :",self.id)
#         print(" name :",self.ename)
#         print(" designation :",self.desig)
#         print(" salary :",self.salary)
#
# emp = employee(101,"hari","ceo",45600)  # auto callinmg of constructor with intilising
# emp.printEmp()


# another example
class student:
    sname = "KENDRIYA VIDAYALAYA KAMPTEE"
    def __init__(self,name,rno,standard):
        self.name = name
        self.rno = rno
        self.sta = standard

    def printVal(self):
        print(" SCHOOL NAME ",student.sname)
        print(" NAME:",self.name)
        print(" ROLL-NO :",self.rno)
        print(" CLASS :",self.sta)

stu = student("rahul",20,"third")
stu.printVal()
