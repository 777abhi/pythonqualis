from Project.proj.circle import Circle
from nose.tools import assert_raises

class TestCircleCreation(unittest.TestCase):

    def test_creating_circle_with_numeric_radius(self):
       # Define a circle 'c1' with radius 2.5, and check if 
        # the value of c1.radius is equal to 2.5 or not.
        c1 = Circle(2.5)
        assert c1.radius==2.5

    def test_creating_circle_with_negative_radius(self):
        # Define a circle 'c' with radius -2.5, and check 
        # if it raises a ValueError with the message
        # "radius must be between 0 and 1000 inclusive".
        c = Circle(-2.5)
        assert c.radius==-2.5
        assert_raises(ValueError)
        

    def test_creating_circle_with_greaterthan_radius(self):
        # Define a circle 'c' with radius 1000.1, and check 
        # if it raises a ValueError with the message
        # "radius must be between 0 and 1000 inclusive".    
        c = Circle(1000.1)
        assert c.radius ==1000.1
        assert_raises(ValueError)
        

    def test_creating_circle_with_nonnumeric_radius(self):
        # Define a circle 'c' with radius 'hello' and check 
        # if it raises a TypeError with the message
        # "radius must be a number".        
        c = Circle(1000.1)
        assert c.radius==1000.1
        assert_raises(ValueError)