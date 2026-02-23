#///findall///
import re

pattern=r"\d+"
text="9 ads 45 hey 20003"
k=re.findall(pattern,text)
print(type(k))
print(k)
