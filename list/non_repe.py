#///printing non repeated//
l=[1,2,2,3,4,4,5]
d={}
#o/p:[1,3,5]
for i in l:
   
        if(i not in d):
            d[i]=1
        else:
            d[i]+=1
for key in d:
    if(d[key]==1):
        print(key)
