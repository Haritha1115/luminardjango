lst = [2,3,8,7,5,1,6,9]
lst1 = [2,3,8,7,5,1,6,9]
new = []
# if the num>6 ouput num+1
# if num<6   output num-1
out1 = list(map(lambda num: num+1 if num < 6 else  num-1, lst1))    # yaha 6==6 vala condition nahi diya
print("out1:",out1)
out3 = list(map(lambda num: num+1 if num<6 else num if num == 6 else num-1, lst))
print("out3:",out3)

for num in lst:
    if num > 6:
        new.append(num-1)
    elif num<6:
        new.append(num+1)
    else:
        new.append(num)
print("using normal",new)
# using list comprehension
out = [i+1 if i<6 else i -1 for i in lst]   # yaha 6==6 vala condition nahi diya
print("out:",out)
out2 = [i+1 if i<6 else i if i==6 else i-1 for i in lst ]
print("out2:",out2)