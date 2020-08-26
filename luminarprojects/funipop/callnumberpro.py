f = open("numbers", "r")
lst = []
even = []
odd = []
for numbers in f:
    numbers = int(numbers.rstrip("\n")) # to remove last char to remove firdt use lstrip
    lst.append(numbers)
print("numbers from file is :", lst)
tot = len(lst)
for i in range(0, tot):
    if lst[i] % 2 == 0:
        even.append(lst[i])
    else:
        odd.append(lst[i])
print ("even list is : ",even)
print("odd list is : ",odd)
