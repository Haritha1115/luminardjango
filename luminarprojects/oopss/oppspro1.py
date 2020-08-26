class empl:
    def setempl(self, id, name, des, sal): #id,name,des,sal are local variable
        self.eid = id
        self.ename = name
        self.desg = des
        self.salary = sal

    def printempl(self):
        print(self.eid)
        print(self.ename)
        print(self.des)
        print(self.sal)


obj = empl()
obj.setempl(101, "hari", "kollam", 25000)
obj.printempl()
# you can use constructor so that u can diresctly give value when object is created
#in line 2 def __init__(arguments)
# .
# .
# .
# and during object call
# obj=empll(101,"hari","kollam",23000)
# just one line
# and only one constructor can be used in one program