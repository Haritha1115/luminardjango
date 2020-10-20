# now we will look for multiple  level inheritance
# class parent:
#     def m1(self):
#         print("i have parent phone")
#
# class child(parent):
#     def m2(self):
#         print(" inside child")
#
# class subchild:
#     def m3(self):
#         print("imside child class")
#
# c = subchild()
# c.m3()
# c.m2()  shows eroor
# c.m1()

# ro slove above issue

class parent:
    def m1(self):
        print("i have parent phone")


class child(parent):
    def m2(self):
        print("inside child")


class subchild(child):
    def m3(self):
        print("imside child class")


s = subchild()
s.m3()
s.m2()
s.m1()

c = child()
c.m2()
c.m1()
# c.m3() # error

p = parent()
p.m1()
# p.m2()  both will be error
# p.m3()



