import re

f = open("emp_detail", "r")
dict = {}
for data in f:
    data = data.rstrip("\n").split(",")
    id = data[0]
    name = data[1]
    desig = data[2]
    sal = data[3]
    dict[id] = {"id": id, "ename": name, "desig": desig, "sal": sal}
print(dict)


def displayfun(**ars):
    print(ars)  # show that data is stored in dictionary
    eid = ars["id"]  # jo arg me id ka value hai usko eid me assign kiya  eid = 1o1
    prop = ars["proper"]  # jo arg me proper  ka value hai usko prop me assign kiya  prop = "desig"
    # if "prop" in ars:
    print(dict[eid]["ename"])  # eid vala key me ename ka key ka value le liye dict->eid->ename
    # else:
    print(dict[eid][prop])  # eid vala key me prop(= desig) ka key ka value le liye dict->eid->prop
# prop me "" isliye nahi laga kyuki prop naam ka koi keyword nahi hai jabki prop = sal ||r explanation f0r eid notin " "

displayfun(id="101", proper="sal")  # pass in string becox it is stored as string so int will not work
