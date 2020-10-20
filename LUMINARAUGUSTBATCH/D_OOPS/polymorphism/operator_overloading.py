# class book :
#     def __init__(self,pages):
#         self.pages = pages
#     def __str__(self):
#         return  str(self.pages)
#
# obj = book(150)
# print(obj)
# obj1 = book(200)
# print(obj1)
# print(obj+obj1)  # it will be error beco obj and obj1 is class book  type object
# so we use __add__ ...in order to subtract 2 obj we can use __sub__ for multiply __mul__ and to divide __truediv__

# solutoion

# class book :
#     def __init__(self,pages):
#         self.pages = pages
#     def __add__(self,other):  # to sub objects __sub__ , to mul __ mul__ , to divide __truediv__
#         return self.pages+other.pages  # give sign according to the operation read
#     def __str__(self):
#         return  str(self.pages)
#
# obj = book(150)
# print(obj)
# obj1 = book(200)
# print(obj1)
# print(obj+obj1)



class book :
    def __init__(self,pages):
        self.pages = pages
    def __add__(self,other):  # to sub objects __sub__ , to mul __ mul__ , to divide __truediv__
        return self.pages+other.pages  # give sign according to the operation read
    def __str__(self):
        return  str(self.pages)

obj = book(150)
print(obj)
obj1 = book(200)
print(obj1)
print(obj+obj1)
obj2 = book(300)
print(obj2)
print(obj+obj1+obj2) # show error as


