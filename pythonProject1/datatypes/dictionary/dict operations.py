"""methods

dict.clear()
dict.copy
dict.fromkeys(iterable,value=None,/)
dict.get(key,default="None")
dict.has_key(key)
dict.items()
dict.keys()
dict.setdefault(key,default="None")#set key to default value if key is not specified
dict.update(dict2)
dict.values()#returns all values
len()
popItem()

"""
dict1={"name":"akhil","age":22,"place":"kottarakkara"}
print(dict1)
p=dict1.clear()
print(dict1)
print("\n")

dict2={"name":'Akhil',"age":22,"place":"kottarakara"}
print(dict2)
p=dict2.copy()
print(p)
print("\n")

dict3={"name":"akhil","age":22,"place":"kottarakara"}
print(dict3)
p=dict.fromkeys(dict3,22)
print(p)
print("\n")

dict4={"name":"akhil","age":22,"place":"kottarakara"}
print(dict4)
print(dict4.get("name"))
print("\n")

dict5={"name":"akhil","age":22,"place":"ktr"}
print(dict5)
del dict5["age"]
print(dict5)

dict6={"name":"cristiano","age":37,"place":"portugal"}
print(dict6)
dict6.popitem()
print(dict6)
