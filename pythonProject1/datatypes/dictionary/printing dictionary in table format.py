dict1={"MATHS":96,"SCIENCE":95,"ENGLISH":92,"MALAYALAM":98}
print("SUBJECT\t\t\t\t\tMARKS\n*****************************")
for key,value in dict1.items():
    if key=="MATHS":
        print(key,"\t\t\t\t\t",value)
    else:
        print(key,"\t\t\t\t",value)