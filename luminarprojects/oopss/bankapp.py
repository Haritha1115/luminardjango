class bank:
    def __init__(self, acc, pname, bal, b_name):
        self.account = acc
        self.name = pname
        self.balance = bal
        self.bankname = b_name

    def printbank(self):
        print("account no: ", self.account)
        print("person name: ", self.name)
        print("balance left: ", self.balance)
        print("bank name: ", self.bankname)

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


n = 0
while n != 1:
    acc = int(input("enter account number :"))
    pname = input("enter person name :")
    bal = int(input("enter your balance :"))
    b_name = input("enter the bank name :")
    m = int(input("want to enter more customer details press 0 for yes and 1 for no : "))
    if m == 0:
        n = 0
    else:
        n = 1
    obj=bank(acc, pname, bal, b_name)
    obj.printbank()
num = int(input("plz enter your choice 1 . withdraw , 2. deposit , 3.enquiery  :"))
if num == 1:
    wd = int(input("enter sum you want to withdraw :"))
    obj.withdraw(wd)
elif num == 2:
    dd = int(input("enter the sum want to deposit :"))
    obj.deposit(dd)
elif num == 3:
    obj.enquiry()
else:
    print("wrong option entered")