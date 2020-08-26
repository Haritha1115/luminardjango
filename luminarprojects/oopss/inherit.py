#example of single inheritance
# class parent:
#     def review(self):
#         print("i have a beutiful family")
#
#
# class child(parent):#agar isme parent nahi diya tuh line 10 galat hoga
#     # kyuki c child ka object hai can only assess o0nly child.but adding parent here it can access
#     pass
#
# c = child()
# c.review()


# example of multi-level inheritance


# class parent:
#     def m1(self):
#         print("inside parent class")
#
# class child(parent):
#     def m2(self):
#         print("inside the child class")
#
# class subchild(child):
#     def m3(self):
#         print("inside subclass")
#
#
# obj = parent()
# obj.m1()
# #obj.m2(),obj.m3() error cant access
# obj1.m1()
# obj.m2()
# #obj1.m3() error cant assess
# obj2 = subchild()
# obj2.m1()
# obj2.m2()
# obj2.m3()

# mutiple heritance
# class parent:
#     def m1(self):
#         print("inside parent class")
#
# class child():
#     def m2(self):
#         print("inside the child class")
#
# class subchild(child, parent):
#     def m3(self):
#         print("inside subclass")

# obj = parent()
# obj.m1() #it will only call this
# obj1 = child()
# obj1.m2() #it will call only this
# obj2 =subchild()
# obj2.m1() # it will call all the functions becoz of line 51
# obj2.m2()
# obj.m3()

# in case of same function name in parent and child
class parent:
    def m1(self):
        print("inside parent class")

class child():
    def m2(self):
        print("inside the child class")

class subchild(child, parent):
    def m3(self):
        print("inside subclass")
