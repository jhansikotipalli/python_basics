#////regex////
#match
import re

pattern=r"^9\d{9}$"
#number="7392285369"
number="9392285369"
k=re.match(pattern,number)
print(type(k))
if(k!=None):
    print(k.start())
    print(k.end())
    print(k.group())
else:
    print("not found")
