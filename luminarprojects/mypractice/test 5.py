lst = [1,2,3,4]
ln = len(lst) -1
num = 6
sm = 0
for i in range(0,ln):
    for j in range(ln, 0,  -1):
        sm = lst[i] + lst[j]
        if lst[i] != lst[j]:
            if num == sm:
                print(lst[i], lst[j])


