myList=[1,2,3,4]
for num in myList:
    if num % 2 == 0:
        print(num)
    else:
        print("odd{num}")

myString="Hello World"
for letter in myString:
    print(letter)

for letter in "Hello":
    print("letter")

tup=(1,3,4)
# for item in tup:
    # print(item)
    
mytup=[(1,2,3),(4,5,6)]
for (a,b,c) in mytup:
    print(a)
    print(b)
    print(c)

myDict={'k1':1,'k2':2,'k3':3}
for key,value in myDict.items():
    print(key)

