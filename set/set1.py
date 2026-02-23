#///set///
s1={1,2,3}
s2={2,4,6,4}
print(s2)
print("max:",max(s2))
print("len:",len(s1))
s2.remove(4)
print(s2)
s1.add(4)
print(s1)
print("union:",s1.union(s2))
print("intersection:",s1.intersection(s2))
print("s1-s2:",s1.difference(s2))
print("s2-s1",s2.difference(s1))
print("symmetric diffenece:",s1.symmetric_difference(s2))
