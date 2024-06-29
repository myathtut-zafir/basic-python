myString="Hello"
myList=[]
for letter in myString:
    myList.append(letter)
print(myList)
myList2=[l for l in myString]
print(myList2)
myList3=[x for x in range(0,11)if x%2==0]
print(myList3)
myList4=[]
for x in [2,4,6]:
    for y in [1,10,300]:
        myList4.append(x*y)

print(myList4)