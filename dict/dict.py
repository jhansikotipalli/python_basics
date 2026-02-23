#///dictionary//
d={"name":"jay","age":24,"add":"hyd"}
print(d)
for key,value in d.items():
    print(f"  {key}:{value}")
print(d["name"])
d2={"class":"first","id":21780}
d.update(d2)
print(d)
del d2
print("add" in d)
del d["class"]
print(d)
print(d.keys())
print(d.values())
print(d.items())
print(len(d))
