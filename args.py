def myFunc(*args):
    return sum(args)*0.05

print(myFunc(40,60,100,1,34))

def myFuncTwo(*args):
    for item in args:
        print(item)
myFuncTwo(1,2,3)

def myFuncKwargs(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit is {}'.format(kwargs['fruit']))
    else:
        print('I have no appoe')

myFuncKwargs(fruit='apple',veggie="lett")

def myfunc(*args):
    return [arg for arg in args if arg % 2 == 0]

# Example usage
even_numbers = myfunc(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(even_numbers)  # [2, 4, 6, 8, 10]
