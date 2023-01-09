txt1="/*Jon is @developer & musician!!"
print("The given string is '",txt1,"'")
result=""
for i in txt1:
    if i.isalpha() is True or i.isspace() is True:
        result=result+i
        continue
    else:
        i="#"
        result=result+i
print("The string after formatting is '",result,"'")