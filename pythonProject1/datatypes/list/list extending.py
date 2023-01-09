list1=['a','b',['c',['d','e',['f','g'],'k'],'l'],'m','n']
sublist=['h','i','j']
print("The given list is ",list1,"\n sublist is ",sublist)
list1[2][1][2].extend(sublist)
print("The list after list extension is ",list1)