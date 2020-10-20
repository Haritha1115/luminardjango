# class parent:
#     def phone(self):
#         print("i have phone")
#
# class child:
#     pass
#
# c = child()
# c.phone()  # show error because child has no access to the parent class def

# so now we will inherit the parent property to class

class parent:
    def phone(self):
        print("i have parent phone")

class child(parent):
    pass

c = child()
c.phone()




