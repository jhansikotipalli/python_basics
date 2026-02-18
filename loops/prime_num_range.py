for n in range(20,31):
    count=0
    for i in range(1,n+1):
        
        if(n%i==0):
            fac=i
            count+=1
    if(count==2):        
        print(f"{n}is prime number")
    else:
        print(f"{n}is not a prime")
