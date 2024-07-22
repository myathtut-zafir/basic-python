import math


class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
        
    def volume(self):
        vol= math.pi * self.radius ** 2 * self.height
        return round(vol, 2)
    
    def surface_area(self):
        result= 2 * math.pi * self.radius * (self.radius + self.height)
        return round(result,1)

    
li = Cylinder(2,3)
print(li.volume())
print(li.surface_area())
