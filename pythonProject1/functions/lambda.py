# str1 = 'Hi Welcome to Kerala'
#
# # lambda returns a function object
# rev_upper = lambda string: string.upper()[::-1]
# print(rev_upper(str1))


# '''# wap to create a lambda fn tht adds 15 to a given number passed as an argument,also create a lambda fn tht mul
#  argument x and y and print the result'''
# n={1,3,5,7}
# add1=lambda num:num+15
# result=map(list(add1(n)))
# print(result)

'''sort a list of tuples using lambda'''
list1=[("akhil"),("jaimon"),("jyothis"),("afin")]
sort1=lambda string:sorted(string)
print(sort1(list1))
