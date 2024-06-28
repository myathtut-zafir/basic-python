with open('myfile.txt', 'w') as file:
    file.write('Hello testing 1234')

myfile=open('myfile.txt')
print(myfile.read())
myfile.seek(0)
print(myfile.read())