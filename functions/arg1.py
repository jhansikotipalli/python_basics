#variable length positional arguments
def add(*arg):
    sum=0
    for i in arg:
        sum+=i
    return sum
    
result=add(1,2,3,4,8)
print(result)

