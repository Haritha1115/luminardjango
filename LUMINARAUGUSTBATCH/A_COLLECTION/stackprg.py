def push(element):
    global top
    if top >= size:
        print("stack is full")
    else:
        stk.append(element)
        top += 1

def pop():
    global top
    if top <= 0:
        print("stack is empty")
    else:
        top = top -1
        print(stk[top],"is popped")


def display():
    global top
    for i in range(0,top):
        print(stk[i])


top = 0
n=1
stk = []
size = int(input("enter the size  of stack :"))
while(n!=0):
    q  = int(input("  1. push  2.pop  3.display : enter your choice :"))
    if q == 1:
        element = int(input("eter the element:"))
        push(element)
    elif q == 2:
        pop()
    elif q == 3:
        display()
    else:
        print("out of option")
    n = int(input("do u want to continue : \n press 1 for yes : \n press 0 for no :"))

