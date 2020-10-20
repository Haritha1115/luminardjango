f= open("ipl.txt","r")
dict = {}
for data in f:
    data  = data.rstrip("\n").split(",")
    # no,team,matches,win,loss,pts
    id = data[0]
    name = data[1]
    match = data[2]
    win = data[3]
    loss = data[4]
    pts = data[5]
    dict[id] = {"name":name,"match" : match,"win":win,"loss":loss,"pts":pts}
print(dict)
def getDetail(**args):
    print(args)
    id = args["id"]
    if "attr" not in args:
        print(dict[id]["name"])
    else:
        attr = args["attr"]
        print(dict[id]["name"])
        print(dict[id][attr])






getDetail(id = "1",attr = "win")