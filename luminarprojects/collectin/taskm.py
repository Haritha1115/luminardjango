#this is done by you... and it worked  ...now let try sir's concept

#lst = []
#for i in range(0, 11):
#    lst.append(i)
#num = int(input("enter the value :"))
#tot = len(lst)
#temp = tot
#for i in range(0,tot):
#    for j in range(i+1,tot):
#        res = 0
#        res = lst[i] + lst[j]
#        if res == num:
#            print(lst[i], lst[j])

lst = [0, 1, 2, 3, 5, 4]
lwr = 0
upp = len(lst)-1
num = int(input("enter a number :"))
while lwr <= upp:
    res = lst[lwr] + lst[upp]
    if num == res:
        print(lst[lwr], lst[upp])
    lwr += 1
    upp -= 1

#here the above one was another idea but problem is it will only prin t one factor not all