# input HHHPPSDAAA    output 3H2P1S1D3A
lst = "HHHPPSDAAA"
char = ""
# for i in lst:                          # even using this many for loop u dont get proper output 3H3H3H2P2P1S1D3A3A3A
#     cnt = 0
#     for j in lst:
#         if i == j:
#             cnt += 1
#     char = char+str(cnt)+i
#
#
# print(char)

dit = {}                              # always use dict for the word count type problem...dont think complicated
for ch in lst:
    if ch not in dit:
        dit[ch] = 1
    else:
        dit[ch] += 1
print(dit)

op = ""
for k, v in dit.items():
    op = op + str(v) + k
print(op)
