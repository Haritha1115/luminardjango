class empl:
    def __init__(self, id, name, des, sal): #id,name,des,sal are local variable
        self.eid = id
        self.ename = name
        self.desg = des
        self.salary = sal

    def printempl(self):
        print(self.eid)
        print(self.ename)
        print(self.desg)
        print(self.salary)


obj = empl(101, "hari", "kollam", 25000)
#obj.setempl(101, "hari", "kollam", 2500)  no need as constructor is called in
# line 2 spo we can directl give valuesat object call
obj.printempl()