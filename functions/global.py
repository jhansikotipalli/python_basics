#//global variable usage//
a=20
def fun():
    
    global a
    a=10
    print(a)
    
def fun2():
    global a
    a=2
    print(a+1)
    
fun()
fun2()       
