class Dog():
    spec="mammal"
    def __init__(self,breed,name) -> None:
        self.breed=breed
        self.name=name

    def bark(self):
        print("woof")

mydog=Dog("t1","mgmg")
print(mydog.bark())

class Circle():
    pi=3.14
    def __init__(self,radius) -> None:
        self.radius=radius
        self.area=radius*radius*self.pi

    def getData(self):
        return self.radius*self.pi*2

mycircle=Circle(30)
print(mycircle.getData())
print(mycircle.area)