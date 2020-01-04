#Define the class Point that represents x, y, and z coordinates of 3D coordinate system.
#Hint : Define the initializer method, __init__ that takes three values and assigns them to attributes x, y and z respectively.
#Now create an object p1 = Point(4, 2, 9) and print it using the statement print(p1).
import numpy

class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return 'point : ('+str(self.x)+', '+str(self.y)+', '+str(self.z)+')'

    def distance(self,x1,x2,y1,y2,z1,z2):
        return numpy.sqrt( (x1-x2)**2 + (y1-y2)**2 + (z1 -z2)**2 )

    def __add__(self,other):
        totalx = self.x+other.x
        totaly = self.y+other.y
        totalz = self.z+other.z
        return Point(totalx,totaly,totalz)
        



#p1 = Point(4,2,9)
#print(p1)

p2 = Point(4, 5, 6)
p3 = Point(-2, -1, 4)

print(p2 + p3)
#print(p2.distance(p2.x,p3.x,p2.y,p3.y,p2.z,p3.z))

#Improvise the class definition of Point such that any Point object is displayed in the format point : (x, y, z).
#Hint : Define the method __str__ inside the class Point.
#Print the object p1 using statement print(p1).


#Define the method distance, inside the class Point, which determines distance between two points. Use formula distance = sqrt( (x1-x2)**2 + (y1-y2)**2 + (z1 -z2)**2 ).
#Create two Point objects p2 = Point(4, 5, 6), p3 = Point(-2, -1, 4) and determine distance of p2 from p3 using defined distance method.
#Print the distance value.

#Improvise Point class definition such that,
#adding any two Point objects using + operator, results in a new Point object with corresponding x, y and z values being added.
#Hint : Define __add__ method inside the class Point.
#Execute the statement print(p2 + p3).