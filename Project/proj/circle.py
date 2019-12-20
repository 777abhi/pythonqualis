import math
class Circle:
    
    def __init__(self, radius):
        # Define initialization method: 
        self.radius = radius
        if (isinstance(self.radius, float)) == False:
            raise TypeError("radius must be a number")
        elif self.radius > 10000 and self.radius < 0:
            raise ValueError("radius must be between 0 and 1000 inclusive")
        
    def area(self):
        # Define area functionality:
        return round(math.pi * self.radius * self.radius,2)
               
    def circumference(self):
        # Define circumference functionality:
        return round(2 * math.pi * self.radius,2)
