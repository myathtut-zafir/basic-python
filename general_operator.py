word='abcde'
for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')
myList=[1,2,4]
myList2=['a','b','c']
for item in zip(myList,myList2):
    print(item) #(1,a)

print('x' in ['x','y']) #True
print('myKey' in {'myKey':345}) #True

myList=[1,2,4,4]
print(min(myList))

# shuffle(myList) random_list

