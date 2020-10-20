# getdetails(statename = kerala, propert = "recovered")
f = open("complete.csv", "r")
dict = {}
for data in f:
    data = data.rstrip("\n").split(",")
    state = data[1]
    recov = data[6]
    dead = data[5]
    confirm = data[4]
    dict[state] = {"recovered":recov,"death":dead,"conformed":confirm}
print(dict)


def getdetails(**args):
    stat = args["state"]
    print(dict[stat]["death"])    # explanation given in idgiven__findname.py
    prop = args["propert"]
    print(dict[stat][prop])

#
# getdetails(state="Kerala")
getdetails(state="Kerala",propert = "recovered")
