# reduce is used fron functool
from functools import *
num = [10, 11, 12, 13, 14]
tot = reduce(lambda num1,num2:num1+num2,num) # 10+11= 21-> 21+12=33 -> 33+13= 46....
print(tot)
# sum can only used with numbers but cant with obect
mx = reduce (lambda num1,num2: num1 if num1>num2 else num2, num) # 1st cmp b/w 10,11 give 11,then b/w 11,12 ,
# the retuen 12,cmp 12,13 retern 13
print(mx)



# reduce me sirf int vales hi allowed hai