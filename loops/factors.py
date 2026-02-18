n=6
count=0
for i in range(1,7):
    if(n%i==0):
        fac=i
        count+=1
        print(f"{n}factors:{fac}")
        
print(f"count of factors for {n}:{count}")

