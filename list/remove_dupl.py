#///remove duplicates///
l=[1,2,2,3,4,4,5]
d={}
for i in l:
    if(i not in d):
        d[i]=1
        
print(d)
print(list(d))
l=list(d)
print(l)
