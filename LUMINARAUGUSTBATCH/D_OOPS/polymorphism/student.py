class student:
    sname = "KENDRIYA VIDAYALAYA KAMPTEE"

    def __init__(self, name, rno, standard):
        self.name = name
        self.rno = rno
        self.sta = standard

    def printVal(self):
        print(" SCHOOL NAME ", student.sname)
        print(" NAME:", self.name)
        print(" ROLL-NO :", self.rno)
        print(" CLASS :", self.sta)

    def __str__(self):  # it is in object class
        #return self.name
        # to also give standard
        return self.name + self.sta   # there is always one written value


stu = student("rahul", 20, "third")
# print(stu) will give a hexadecimal value s
# here we are printing object __str__(self) it is called tostring() method
# to print the name or another info simply by printing the obj we use __str__
print(stu)
