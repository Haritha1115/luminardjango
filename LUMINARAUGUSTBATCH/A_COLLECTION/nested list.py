employee = [[100,"tarun",20000],[101,"varun",32000],[102,"taniya",45000]]

#here it will print each listed elemrnt
# for data in employee:
#     print(data)

# to just print ename
# for data in employee:
#     print(data[1])


# inside the for loop
# [[100,"tarun",30000],      [101,"varun",32000],      [102,"taniya",45000]]
#  data[0],data[1],data[2]    data[0],data[1],data[2]   data[0],data[1],data[2]
#    data @ first loop          data at second loop         data at third loop

# to calulate the sal
# tot = 0
# for data in employee:
#     tot += data[2]
# print(tot)

# to print ename whose sal >25k
# for data in employee:
#     if (data[2]>25000):
#         print(data[1])