#///subn///
import re
line="hiii      everyone    !   "
pattern=r"\s+"
result=re.subn(pattern," ",line)
print(result)
print(type(result))
