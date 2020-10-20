# class parent:
#     def phone(self):
#         print("i have parent phone")
#
# class child(parent):
#     pass
#
# c = child()
# c.phone()   # parent vala work hoga

# now child has a phone()
class parent:
    def phone(self):
        print("i have parent phone")

class child(parent):
    def phone(self):      # method overriding  # agar child to naya method chahiye tuh usko child me overwrite karna hoga
        print("i have my  phone")

c = child()
c.phone() # now child vala phone work karega

# parent->child
# superclass -> sub_class
# base class -> derived class
