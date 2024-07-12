def square(num):
    return num*2
my_nums=[1,2,3,4,5]
for i in map(square,my_nums):
    print(i)

print(list(map(square,my_nums)))

def check_even(num):
    return num%2==0

mynums=[1,2,3,4,5,6]
print(list(filter(check_even,mynums)))
# nameless func
square=lambda num: num**2
print(square(3))
names=['mgmg','kyaw','mya']
print(list(map(lambda name:name[0],names)))