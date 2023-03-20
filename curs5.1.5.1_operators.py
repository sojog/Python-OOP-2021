class Point:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    
    def __add__ (self, anotherPoint):
        return Point(self.x+anotherPoint.x, self.y+anotherPoint.y)

    def __eq__ (self, anotherPoint):
        return self.x == anotherPoint.x and self.y == anotherPoint.y

    def __str__ (self):
        return "Point at coordinates: (" + str(self.x)+ "," + str(self.y) + ")" 


point1 = Point(3,2)
point2 = Point(2,3)
#print(point1 + point2)
print(point1 == point2)








