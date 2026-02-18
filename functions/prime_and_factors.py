#/////given no. is prime or not and print factors of that number////
def is_prime(n):
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            fac=i
            print(f"{n} factor :{fac}")
            count+=1
    if(count==2):
        return 1
    else:
        return 0
n=6
if(is_prime(n)):
    print("prime")
else:
    print("not prime")
