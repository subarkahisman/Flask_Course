from math import pi

class Circle(object):
    def __init__(self):
        self.radius = 0
        
    def setRadius(self, r):
        self.radius = r
        
    def getRadius(self):
        return self.radius
        
    def area(self):
        return pi * (self.radius ** 2)
        
    def circumference(self):
        return 2 * pi * self.radius 
    