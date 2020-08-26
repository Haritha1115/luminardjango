lst = [1, 2, 3, 4, 5, 6, 7]

# use of map

# def sq(num):
#     return num*num
# sqr = list (map(sq,lst)  # ...............line 1
# print(sqr)

# use of filter

# def even(num):
#     return (num % 2 == 0)
#
#
# evn = list(filter(even, lst))  #..................line 2
# print(evn)

# use of labda line 1 and line 2
sqt = list(map(lambda num: num * num, lst))
print(sqt)
