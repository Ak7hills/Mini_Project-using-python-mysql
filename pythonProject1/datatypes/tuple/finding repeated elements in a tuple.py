tpl1=(1,2,2,3,3,3,5,7,8,9)
set1=set(tpl1)
for i in tpl1:
    if i in set1:
        p=tpl1.count(i)
        if p>1:
            print("the element",i,"is seen",p,"times")
            set1.remove(i)
    else:
        pass
