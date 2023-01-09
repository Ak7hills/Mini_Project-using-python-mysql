str1="HeLlo woRld"
lower=''
upper=''
for i in str1:
    if(i.isupper==True):
         upper=upper+i
    elif(i.islower==True):
         lower=lower+i
    else:
        continue
print("lower case:",lower)
print("upper case:",upper)









"""
Difference b/w list and tuple

list is a datatype in which the elements are contained within a "[]"
list is mutable
eg:a=[1,345,554]

tuple is a datatype in which the elements are contained within a "()"
tuple is immutable
tuple is unordered
eg: a=(28,184,28)
"""
