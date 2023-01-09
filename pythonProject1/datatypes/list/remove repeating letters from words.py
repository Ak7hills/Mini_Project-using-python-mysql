str1="Let's google the pineapple"
print("The given string is '",str1,"'")
splitstr1=str1.split(" ")
#print(splitstr1)
#print(type(splitstr1))
newlist=[]
for word in splitstr1: #word=lets,google,the,pineapple
    t=''
    for i in word:
        if i in t:
            continue
        else:
            t=t+i
    newlist.append(t)
    #print(newlist)
output=" ".join(newlist)
print("The string after formatting is '",output,"'")