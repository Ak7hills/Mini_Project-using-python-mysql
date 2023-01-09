my_tuple=( )
print(my_tuple)
tuple1=(1,"akhil",22,[3,6,9])
print(tuple1)
print(tuple1[3][0])
tuple1[3].append(4)
print(tuple1)
print(len(tuple1))
print(all(tuple1))
print(tuple1[::-1])
"""all
any
enumerate
len
max
min
sorted
sum
tuple"""
print(tuple1[1:3])
print(list(tuple1))
a=("apple","banana","orange")
alist=list(a)
alist.insert(1,"grape")
a=tuple(alist)
print(a)

b=("akhil",22)
y=enumerate(b)
print(list(y))
print(len(b))
c=(11,15,78,34)
print(max(c))
print(min(c))
print(sorted(c))
print(sum(c))

