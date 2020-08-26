# def add(num1, num2):
#     return (num1 + num2)
#
#
# print(add(10, 20))

# using lamda function we can reduce the lines

f = lambda num1, num2,num3,num4: num1 + num2 + num3 +num4
print(f(10, 30, 40, 50))  # 40

h = lambda num1, num2: num1 * num2
print(h(10, 30))  # -20 for sub ,//////   while multiply ans 300

g = lambda num1, num2, num3, num4: num1 - num2 - num3 - num4
print(g(10, 30, 40, 50))

