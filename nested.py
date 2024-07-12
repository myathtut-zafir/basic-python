name="Global"

def greet():
    name='Sammy'
    def hello():
        print('Hello '+name)
    hello()

def greetTwo():
    def hello():
        global name #override the global var
        name="ddasdsad"
        print('Hello '+name)
    hello()
print(greetTwo())
print(name)