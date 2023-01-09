str1=["John","","emma","","Jins","Lina"]
print("The given string is ",str1)
for i in str1:
    if i.isalpha() is True:
        pass
    else:
        str1.remove(i)
print("The string after formatting is",str1)