#power of n
def power(a,n):
    if(n==0):
        return 1
    return a*power(a,n-1)
k=power(5,3)
print(f"5 power of 3 is:{k}")
