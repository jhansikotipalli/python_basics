#///finditer///
import re
pin="12abc33efgh900"
pattern=r"\d{2}"
k=re.finditer(pattern,pin)
if(k!=None):
    for i in k:
        print(i.start(),i.end(),i.group())
        
else:
    print("not found")


