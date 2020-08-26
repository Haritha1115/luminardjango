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

    def __str__(self): # description written in book
        return self.name # we override function  becoz we dont need memory we need diff output

obj = bank(1001,"ram",50000,"axis")
print(obj)

#outoput me hexadecimal value hoga it is m/o value not the ecxact m
# one due to  security problem due to authentication
