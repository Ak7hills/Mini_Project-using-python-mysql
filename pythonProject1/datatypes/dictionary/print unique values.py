listdict=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
setofuvalues=set()
for i in listdict:
    for value in i.values():
        setofuvalues.add(value)
print(setofuvalues)