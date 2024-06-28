print("I\n!")
print(len("ddd"))
 # type: ignore

#  string indexing
myString='hello'
print(myString[0])
#  string reverse indexing
myString='helAo'
print(myString[-2])
#  index
myString='hello'
print(myString[:4]) #hell
print(myString[1:4]) #ell
print(myString[::1]) #need to learn more
print(myString[::-2]) #need to learn more
# method
# immutability
name='myat'
# name[0]="J"# found error because string obj are immutability
# concat string
last_letter=name[1:]
print(last_letter)
print('m'+last_letter)
print(name.capitalize()) # string method

# print string
print('The {0} {1} {2}'.format("A","B","C"))
print('The {a} {b} {c}'.format(a="A",b="B",c="C"))

name="John"
print(f'The is {name}')



