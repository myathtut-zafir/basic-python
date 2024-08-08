def gen_fibon(n):
    a=1
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b

# for number in gen_fibon(10):
    # print(number)

def simple_gen():
    for x in range(3):
        yield x

# for number in simple_gen():
#     print(number)

g=simple_gen()
print(next(g))
print(next(g))

s="hello"
# for letter in s:
#     print(letter)

sIter=iter(s) # next for string
print(next(sIter))


