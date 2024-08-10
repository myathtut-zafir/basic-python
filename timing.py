import time
import timeit
def func_one(n):
    return [ str(num) for num in range(n)]

def func_two(n):
    return list(map(str,range(n)))

start_time=time.time()
result=func_one(100)
end_time=time.time()
elapsed_time=end_time - start_time
print(elapsed_time)


start_time=time.time()
result=func_two(100)
end_time=time.time()
elapsed_time=end_time - start_time
print(elapsed_time)


stmt='''
func_one(100)
'''
setup='''
def func_one(n):
        return [ str(num) for num in range(n)]
'''
print(timeit.timeit(stmt,setup,number=100000))

stmtTwo='''
func_two(100)
'''
setupTwo='''
def func_two(n):
        return list(map(str,range(n)))
'''
print(timeit.timeit(stmtTwo,setupTwo,number=100000))