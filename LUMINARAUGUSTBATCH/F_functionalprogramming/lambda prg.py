# def add(num1,num2):
#     return num1+num2
#
# n = add(10,20)
# print(n)

#1. lambda / anonymous function  (nameless)
# def (num1,num2):  # remove add and and def and return
#     return num1+num2

f = lambda num1,num2:num1+num2
print(f(10,50))

f1 = lambda num1,num2:num1-num2
print(f1(100,50))

f2 = lambda num1,num2:num1*num2
print(f2(20,30))

f3 = lambda num1,num2: num1/num2
print(f3(900,30))

cube = lambda num: num**3
print(cube(4))