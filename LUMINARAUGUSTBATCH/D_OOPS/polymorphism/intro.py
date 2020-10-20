# plymorphism = many forms
# 1. method overloading
# 2.method overriding
# 3. operator overloading
#
# 1. method overloading
class maths:
    def add(self):
        num1, num2 = 10,20
        print(num1+num2)
    def add(self,num1):
        num2 = 30
        print(num1+num2)
    def add (self,num1,num2):
        print(num1+num2)

ob = maths()
#ob.add()  # these 2 will show error
# ob.add(10)
ob.add(40,50) # only last one worked recent one