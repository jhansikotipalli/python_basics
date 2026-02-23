    
#///fullmatch///
import re

pattern=r"1[0-9]{2}"
text="102"
k=re.fullmatch(pattern,text)
print(type(k))
print(k)
