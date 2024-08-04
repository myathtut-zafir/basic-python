
def hello(name="myat"):
    print("Hello execute!")
    def greet():
        return '\t this is greet() inside hello func'
    def welcome():
        return '\t this is welcome() inside hello func'
    print("return func")
    if name=="myat":
        return greet
    else:
        return welcome
    
    # print(greet())
    # print(welcome())
    # print("this is the end")


myFunc=hello()
# print(myFunc)
print(myFunc())

def hi():
    return "Hi!"
def other(some_func):
    print("other code run here")
    print(some_func())

tt=other(hi)
print(tt)

#python decro
def new_decro(original_func):
    def wrap_func():
        print("some extra code before")
        original_func()
        print("some extra code after original func")
    return wrap_func

@new_decro
def func_needs_decorator():
    print("I want to be decor")

print(func_needs_decorator())