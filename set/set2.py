s=set()
s.add(1)
s.update([3,4,5])
print(s)
#s.remove(2)error
s.discard(2)#if not found no error
print(s)
for item in s:
    print(item)
