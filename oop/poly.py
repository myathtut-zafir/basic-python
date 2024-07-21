class Animal():
    def __init__(self) -> None:
        print("ANIMAL CLASS")
    def who(self):
        print("I am Animal")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("DOG Created")
    def who(self):
        print("I am dog")

myanimal=Dog()
print(myanimal.who())