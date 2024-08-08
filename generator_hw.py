import random


def gensquares(n):
    for n in range(n):
        yield n**2

# for number in gensquares(10):
#     print(number)


def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low, high)
        
for num in rand_num(1,10,12):
    print(num)

s='hello'
siter=iter(s)
print(next(siter))


my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)
