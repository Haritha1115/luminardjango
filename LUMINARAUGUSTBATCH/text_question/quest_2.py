# in temp file there are two times the name and given is given ..so you have to display the max temp of particular state
f = open("temp", "r")
lst = []
new = []
for data in f:
    data = data.rstrip("\n").split(",")
    state = data[0]
    tmp = data[1]
    lst.append(state)
    lst.append(int(tmp))
print(lst)
n = int(len(lst)//2)
print(n)
i = 0
while (i <= n-1) & (n < len(lst)):
    if lst[i] == lst[n]:
        new.append(lst[i])
        z = max(lst[i+1], lst[n+1])
        new.append(z)
    i += 2
    n += 2
print(new)
