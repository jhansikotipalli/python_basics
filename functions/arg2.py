def add(x,y):
    return x+y
def msg(name,age):
    print(f"hi {name} ur {age} years old")
def display(name,age=22):
    print(f"hi {name} ur {age} years old")
    
def sum(*arg):
    print(type(arg))
    sum=0
    for i in arg:
        sum+=i
    return sum

def screen(**kwarg):
    print(type(kwarg))
    for i in kwarg.keys():
        print(f"{i}:{kwarg[i]}")

k=add(10,20)
print(k)
msg(22,"jaya")
msg("jhansi",24)
msg(name="hema",age=25)
display(name="jhansi",age=23)
display(name="krish")
result=sum(10,20,30)
print(result)
result1=sum(34,45)
print(result1)
screen(name="ram",age=26,id=12345,status="married")
