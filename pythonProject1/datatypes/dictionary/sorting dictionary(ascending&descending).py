dict1={1:2,3:4,4:3,2:1,0:0}
print("The given dictionary is :",dict1,"\n")
val=list(dict1.items())
newval=[]
newvalf=[]
for i in val:
    irev=i[::-1]
    newval.append(irev)
#print(newval)
val.clear()
newval.sort()
for i in newval:
    irevf=i[::-1]
    val.append(irevf)
#print(val,"/n")
for i in (newval[::-1]):
    i=i[::-1]
    newvalf.append(i)
#print(newvalf,"/n")
print("The dictionary in ascending order of key values: ",val,"\n")
print("The dictionary in descending order of key values: ",newvalf)
