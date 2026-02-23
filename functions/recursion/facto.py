#//factorial//
def fac(n):
    if(n==1):
        return 1
    return n*fac(n-1)
k=fac(5)
print(f"5 factorial is:{k}")
