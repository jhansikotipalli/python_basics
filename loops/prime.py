n=5
for i in range(1,11):
    count=0
    if(n%i==0):
        fac=i
        count+=1
if(count==2):        
    print(f"{n}is prime number")
else:
     print(f"{n}is not a prime")
