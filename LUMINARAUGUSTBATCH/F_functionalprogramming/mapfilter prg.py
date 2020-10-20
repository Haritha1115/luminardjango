# map,filter,reduce


name = ["ajay", "anu", "hari", "binu"]
# each opbject then to upper case
# in this we can use map (here for each input we have corresponding output)
# in filter (used when we have not to generate no.of output != no of input)
# reduce (for single value output like sum,min,max)

num = [2, 4, 6, 8, 7, 9]


# to find the no*2 we use map
# to find even/odd  we use filter we are filtering number
# to find sum/max/min we use reduce

# to ca;lculate sq of each no.
# map has 2 argument(function ,iterable/list/jispe operation karna hai)
def square(num):
    return num ** 2


# data = map(square,num)  #<map object at 0x01A9B028>  <-oupout :::: so to get proper output we use list
# data = list(map(square,num))
# square = lambda num:num*num
data = list(map(lambda num: num * num, num))
print(data)


# to find even
def even(num):
    return num % 2 == 0


# evn = list(filter(even,num))
# even  = lambda num:num%2 == 0
evn = list(filter(lambda num: num % 2 == 0, num))
print(evn)

# to print all to upper

lst = ["kkr", "hari", "ghy", "hdj"]
cap = list(map(lambda str: str.upper(), lst))
print(cap)
