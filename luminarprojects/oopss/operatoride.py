class book:
    def __init__(self,pages):
        self.pages = pages

    def __str__(self):
        return str(self.pages)

    def __add__(self,others):
        return (self.pages + others.pages)

ob = book(100)
ob2 = book(200)
print(ob+ob2)
# to add three object print (ob+ob2+ob3)
