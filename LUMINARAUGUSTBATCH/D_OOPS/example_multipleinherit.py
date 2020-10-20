class person:
    def setperson(self, name, age):
        self.name = name
        self.age = age

    def printperson(self):
        print("name:", self.name)
        print("age:", self.age)


class Bank(person):
    bname = "federal"

    def setValues(self, accno, bal):
        self.ano = accno
        self.bal = bal

    def createAccount(self):
        print("\nCONGRATS!! YOUR NEW ACCOUNT IS CREATED")
        print("you have selcted bank :", Bank.bname)  # to access tge stactic variable # self .bane nahi hoiga
        # kyuki now bname is static variable not a instance
        print("your account number :", self.ano)

    def withDraw(self, bal, wdraw):
        tot = 0
        if self.bal > 10000:
            tot = self.bal - wdraw
            print("\nTotal balance left :", tot)
        else:
            print("\ncant withdraw, balance is less than 10K")

    def deposit(self, bal, dpt):
        tot = self.bal + dpt
        print(" new balance :", tot)

    def balanceEnquiry(self, bal):
        print("current balance:", bal)


obj = Bank()
# obj.setperson("ajay", 23)
# obj.printperson()    obj of bank call function of parant person clas
x = 1
print("\nENTER YOUR DETAILS:")
pername = input("enter person name: ")
age = input("enter age:")
accno = input("enter the acc_no: ")
bal = int(input("enter balance: "))
obj.setValues(accno, bal)
obj.setperson(pername, age)  # object of child class calling parent class function due to inheritance
while x != 0:
    n = int(input("\nENTER YOUR CHOICE \n 1. create account \n 2.withdraw \n 3. deposit \n 4.balance enquiry"))
    if n == 1:
        obj.createAccount()
    elif n == 2:
        wdraw = int(input("\n enter the amount to be withdraw :"))
        obj.withDraw(bal, wdraw)
    elif n == 3:
        dep = int(input("\n enter deposit amount :"))
        obj.deposit(bal, dep)
    elif n == 4:
        obj.balanceEnquiry(bal)
    x = int(input("\nif u want to continue press 1 or to exit press 0"))
