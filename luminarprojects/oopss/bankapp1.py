class person:
    def setvalues(self, pname, age):
        self.name = pname
        self.ag = age
    def printperson(self):
        print("name :",self.name)
        print("age :",self.ag)


class bank(person):
    bname = "axis"
    def __init__(self, acc, bal):
        self.account = acc
        self.balance = bal

    def printbank(self):
        print("account no: ", self.account)
        print("balance left: ", self.balance)
        print("person name :", self.name)
        print("bank name :", bank.bname)

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print("amount left after withdraw :", self.balance)
        else:
            print("amount insufficent to withdraw")

    def deposit(self, damount):
        self.balance += damount
        print("new balance is:", self.balance)

    def enquiry(self):
        print("your current balance is:", self.balance)


# n = 0
# while n != 1:
#     acc = int(input("enter account number :"))
#     pname = input("enter person name :")
#     bal = int(input("enter your balance :"))
#     b_name = input("enter the bank name :")
#     m = int(input("want to enter more customer details press 0 for yes and 1 for no : "))
#     if m == 0:
#         n = 0
#     else:
#         n = 1
#     obj = bank(acc, pname, bal, b_name)
#     obj.printbank()
# num = int(input("plz enter your choice 1 . withdraw , 2. deposit , 3.enquiery  :"))
# if num == 1:
#     wd = int(input("enter sum you want to withdraw :"))
#     obj.withdraw(wd)
# elif num == 2:
#     dd = int(input("enter the sum want to deposit :"))
#     obj.deposit(dd)
# elif num == 3:
#     obj.enquiry()
# else:
#     print("wrong option entered")

obj = bank(1001,24503) #single object 
obj.setvalues("hari", 23)
obj.printperson()
obj.setvalues(1001, 20000)
obj.printbank()
# obj.deposit(3000)
# obj.enquiry()
# obj.withdraw(3003)
# obj.enquiry()
