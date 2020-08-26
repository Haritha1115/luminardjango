import functools
lst = [10,20,30,45,65,34,56]
sm = functools.reduce(lambda num1,num2:num1+num2,lst)
print(sm)
dif = functools.reduce(lambda num1,num2:num1-num2,lst)
print(dif)
max = functools.reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
print(max)
min = functools.reduce(lambda num1,num2:num2 if num1>num2 else num1,lst)
print(min)