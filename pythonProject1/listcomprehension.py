"""1.find the common numbers in two list1=[1,2,3] list2=[3,4,5]
2.count no. of spaces in the string
3.find all words in a string that are less than 4 letters
4.use a nested list comprehensiono find all of the no. from 1 to 1000 that are divisible by any single digit other than one"""
#1
list1=[1,2,3,4]
list2=[2,3,4,5]
com=[x for x in list1 if x in list2]
print(com)

#2
str1="how are you"
a=[x for x in str1 if x.isspace()]
print(a)

#3
text="India is my country"
a=text.split()
result=[x for x in a if len(x)<4]
print(result)