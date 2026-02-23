#///search///
import re
pin="abc33efgh900"
pattern=r"\d{2}"
k=re.search(pattern,pin)
if(k!=None):
    print(k.start())
    print(k.end())
    print(k.group())
else:
    print("not found")

