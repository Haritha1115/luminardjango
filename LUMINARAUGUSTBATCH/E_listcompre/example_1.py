lst = [1, 2, 3, 4]
lst2 = [6, 7, 8, 9]
# (1,6),(1,7)(1,8)(1,9)
# for i in lst:
#     for j in lst2:
#         print(i, j)

output = [(i, j) for i in lst for j in lst2]
print(output)
# to find the squares
out1 = [i * i for i in lst]  # out1 = list(map(lambda num : num**2,lst)) using map
print(out1)
out2 = [i for i in lst if i % 2 == 0]  # dont put if condition in front o0f for
print(out2)
