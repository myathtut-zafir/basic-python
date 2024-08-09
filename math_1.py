import math
from math import pi
import random


values=4.35
print(math.floor(values))
print(math.ceil(values))
print(round(values))

# print(pi)
# print(math.log(math.e))
# print(random.randint(0,100))
print(random.seed(101))
print(random.randint(0,100))
print(random.randint(0,100))

myList=[1,2,3,4,5,6,7,8,9,0,11,12,13,10]
# print(random.choice(myList))
print(random.choices(population=myList,k=10))
print(random.sample(population=myList,k=10))




