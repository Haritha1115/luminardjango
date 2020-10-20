# class Bank:
#     def setValues(self,bankname,pername,accno,bal):
#         self.bname = bankname
#         self.pname = pername
#         self.ano = accno
#         self.bal = bal
#
#     def createAccount(self):
#         print("\nCONGRATS!! YOUR NEW ACCOUNT IS CREATED")
#         print("you have selcted bank :",self.bname)
#         print("your account name :",self.pname)
#         print("your account number :",self.ano)
#
#     def withDraw(self,bal,wdraw):
#         tot = 0
#         if self.bal > 10000:
#             tot = self.bal - wdraw
#             print("\nTotal balance left :",tot)
#         else:
#             print("\ncant withdraw, balance is less than 10K")
#
#     def deposit(self,bal,dpt):
#         tot = self.bal + dpt
#         print(" new balance :",tot)
#
#     def balanceEnquiry(self,bal):
#         print("current balance:",bal)
#
#
# obj = Bank()
# x = 1
# print("\nENTER YOUR DETAILS:")
# bankname = input("enter bank name:")
# pername = input("enter person name: ")
# accno = input("enter the acc_no: ")
# bal = int(input("enter balance: "))
# obj.setValues( bankname,pername,accno,bal)
# while x != 0:
#     n = int(input("\nENTER YOUR CHOICE \n 1. create account \n 2.withdraw \n 3. deposit \n 4.balance enquiry"))
#     if n ==1:
#         obj.createAccount()
#     elif n ==2:
#         wdraw = int(input("\n enter the amount to be withdraw :"))
#         obj.withDraw(bal, wdraw)
#     elif n ==3:
#         dep = int(input("\n enter deposit amount :"))
#         obj.deposit(bal,dep)
#     elif n ==4:
#         obj.balanceEnquiry(bal)
#     x = int(input("\nif u want to continue press 1 or to exit press 0"))


# if we have same bank name
# instance variable = self.bame ,self. variable  are static variable...... they always  are related to object
# here we have a common bank name and as we give it each time memory is wasting so  ...
# in order to access the bank name by all   we declare bank as static variable
# class ke niche  bankname = "federal"
# static is used for the better  memory location

class Bank:
    bname = "federal"
    def setValues(self,pername,accno,bal):
        self.pname = pername
        self.ano = accno
        self.bal = bal

    def createAccount(self):
        print("\nCONGRATS!! YOUR NEW ACCOUNT IS CREATED")
        print("you have selcted bank :",Bank.bname) # to access tge stactic variable # self .bane nahi hoiga
        # kyuki now bname is static variable not a instance
        print("your account name :",self.pname)
        print("your account number :",self.ano)

    def withDraw(self,bal,wdraw):
        tot = 0
        if self.bal > 10000:
            tot = self.bal - wdraw
            print("\nTotal balance left :",tot)
        else:
            print("\ncant withdraw, balance is less than 10K")

    def deposit(self,bal,dpt):
        tot = self.bal + dpt
        print(" new balance :",tot)

    def balanceEnquiry(self,bal):
        print("current balance:",bal)


obj = Bank()
x = 1
print("\nENTER YOUR DETAILS:")
pername = input("enter person name: ")
accno = input("enter the acc_no: ")
bal = int(input("enter balance: "))
obj.setValues(pername,accno,bal)
while x != 0:
    n = int(input("\nENTER YOUR CHOICE \n 1. create account \n 2.withdraw \n 3. deposit \n 4.balance enquiry"))
    if n ==1:
        obj.createAccount()
    elif n ==2:
        wdraw = int(input("\n enter the amount to be withdraw :"))
        obj.withDraw(bal, wdraw)
    elif n ==3:
        dep = int(input("\n enter deposit amount :"))
        obj.deposit(bal,dep)
    elif n ==4:
        obj.balanceEnquiry(bal)
    x = int(input("\nif u want to continue press 1 or to exit press 0"))