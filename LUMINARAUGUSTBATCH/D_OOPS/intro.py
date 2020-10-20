class Person:  # always give the first character of classname as capital
    def setValues(self, nam, ag):  # self keyword becoz it is inside class
        self.age = ag  # self.age = age which we passed in parameter during function call
        self.name = nam  # self.name = name which we passed in parameter during function call

    def printValues(self):
        print("age:", self.age)
        print("name:", self.name)

# self is used to point the current class instance /current object 
# while defining function:first char of first word will be small(set) and first char of second word will be caps(Values)
obj = Person()
obj.setValues("Haritha",23)
obj.printValues()
obj1 = Person()
obj1.setValues("Harsha",22)
obj1.printValues()