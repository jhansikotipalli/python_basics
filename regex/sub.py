#///sub//
import re
line="hiii      everyone    !   "
pattern=r"\s+"
result=re.sub(pattern," ",line)
print(result)
print(type(result))
