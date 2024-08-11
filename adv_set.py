s=set()
s.add(1)
s.add(2)
s.clear()
print(s)

s={1,2,3}

s.add(5)
sc=s.copy()
print(sc)
print(s.difference(sc))
s1={1,2,3}
s2={1,5,3}
s1.difference_update(s2)
print(s2)

s3={1,2,3}
s4={1,2,4}
print(s3.intersection(s4)) # take same value

s5={1,2}
s6={1,2,4}
s7={5}
print(s5.isdisjoint(s7))


s1={1,2}
s2={1,2,4}
s3={5}
print(s1.union(s2))


