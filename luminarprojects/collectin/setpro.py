# to remove duplicate from list a short method using sets, main one is in removedupli.py
# lst = {10, 90, 30, 28, 10, 66, 66, 23, 45, 45}
# st = set(lst)                   declaring a set
# print(st)

# using set operation
# 1.union
st = {1, 2, 3, 4, 5, 6, 7, 8}
st2 = {6, 7, 8, 9, 10, 11}
# un = st.union(st2)
# print(un)

# 2.intersection
# un= st.intersection(st2)
# print(un)

# 3.difference
un = st.difference(st2)
print(un)
