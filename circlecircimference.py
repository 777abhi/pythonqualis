# Define the class 'Circle' and its methods with proper doctests:
import re

class Circle:
    def __init__(self, radius):
        # Define doctests for __init__ method:
        """
        >>> c1 =Circle(2.5)
        >>> c1.radius
        2.5
        """
        self.radius = radius
        
    def area(self):
        # Define doctests for area method:
        """
        >>> c1 = Circle(2.5)
        >>> c1.area()
        19.63
        """
        # Define area functionality:
        import math
        return round(math.pi * self.radius * self.radius,2)

    def circumference(self):
        # Define doctests for circumference method:
        """
        >>> c1 = Circle(2.5)
        >>> c1.circumference()
        15.71
        """
        # Define circumference functionality:
        import math
        return round(2 * math.pi * self.radius,2)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    import inspect
    c2 = Circle(2.5)
    doc1 = inspect.getdoc(c2.__init__)
    doc2 = inspect.getdoc(c2.area)
    doc3 = inspect.getdoc(c2.circumference)
   # print(doc1)
    
    class_count = len(re.findall(r'Circle', doc1))
    func1_count = len(re.findall(r'c1.radius', doc1))
    func1_val = len(re.findall(r'2.5', doc1))
    
    print(str(class_count), str(func1_count), str(func1_val))
    
  #  print(doc2)
    class_count = len(re.findall(r'Circle', doc2))
    func1_count = len(re.findall(r'c1.area', doc2))
    func1_val = len(re.findall(r'19.63', doc2)) 
                      
    print(str(class_count), str(func1_count), str(func1_val))
                      
 #   print(doc3)
    
    class_count = len(re.findall(r'Circle', doc3))
    func1_count = len(re.findall(r'c1.circumference', doc3))
    func1_val = len(re.findall(r'15.71', doc3)) 
                      
    print(str(class_count), str(func1_count), str(func1_val))
