#// gcd//
def gcd(m,n):
    if(n==0):
        return m
    return gcd(n,m%n)
k=gcd(49,14)
print(f"48,14 gcd:{k}")

