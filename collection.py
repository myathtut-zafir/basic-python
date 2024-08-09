
from collections import Counter
from collections import defaultdict
from collections import namedtuple


myList=[1,1,1,1,1,1,2,2,2,2,2,3,4,4,4,4]
print(Counter(myList))
str="aaaaaaa"
print(Counter(str))

letters="aasfsfasfsaff"
c=Counter(letters)
print(c.most_common(2))
print(list(c))

d=defaultdict(lambda:0)
d['coo']=10
print(d['coos'])

mytuple=(10,20,30)
Dog=namedtuple('Dog',['age','breed','name'])
sammy=Dog(age=5,breed="Hus",name="sammy")
print(sammy.age)
print(sammy[0])