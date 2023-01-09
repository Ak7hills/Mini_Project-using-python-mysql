str1="luminar"
print("The given string is :",str1)
dict1={}
for index in range(1,len(str1)+1):
    dict1.setdefault(index,str1[index-1])
print("The dictionary of given string is:",dict1)
