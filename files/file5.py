with open("file.txt","r") as f:
    content=f.read()
ccount=len(content)
wcount=len(content.split())
lcount=len(content.splitlines())
print("ccount:",ccount)
print("word count:",wcount)
print("line count:",lcount)
print("is file closed?:",f.closed)
