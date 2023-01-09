str1 = input("Input words: ")

str1_list= str1.split(",")
str1_list.sort()
print((', ').join(str1_list))