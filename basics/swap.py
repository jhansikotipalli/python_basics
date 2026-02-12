#swapping of two numbers
#method 1
a=10
b=20
a,b=b,a
print(f"a value is {a}")
print(f"b value is {b}")

#method 2


a=10
b=20
temp=a
a=b
b=temp
print(f"a value {a}")
print(f"b value {b}")

#method 3
a=10
b=20
a=a+b
b=a-b
a=a-b
print(f"a value {a}")
print(f"b value {b}")

#method 4
a=10
b=20
a=a^b
b=a^b
a=a^b
print(f"a value {a}")
print(f"b value {b}")


