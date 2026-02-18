def is_even(n):
    if(n%2==0):
        return 1
    else:
        return 0
n=16
c=is_even(n)
if(c):
    print(f"{n} number is even")
else:
    print(f"{n} is odd")

