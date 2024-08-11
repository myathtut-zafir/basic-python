d={"k1":1,"k2":2}
print({x:x**2 for x in range(10)})
print({k:v for k,v in zip(['a','b'],range(2))})

for k in d.keys():
    print(k)
