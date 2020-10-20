class parent1:
    def m1(self):
        print("i have parent phone")


class parent2:
    def m1(self):
        print("inside parent")


class child(parent1,parent2):
    def m3(self):
        print("imside child class")

c = child()
c.m3()
c.m1()# yaha 2 m1()hai so complier ko confusion hoga it is called ambiguity (main problem of java thats why it dont supoort this)
 # here in pyhthon it will print the m1() of first parent1 to avoid the conflict