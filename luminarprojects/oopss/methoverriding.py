class parent:
        def phone(self):
            print ("have latest phone")

class child(parent):
    def phone(self):
        print("iphone")


c=child()
c.phone()