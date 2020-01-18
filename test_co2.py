#Define the function isEven which returns True, if a given number is even and returns False, if the number is odd.
#Execute the statement isEven(43) and display the output.

#Define a class TestIsEvenMethod, which is derived from unittest.TestCase class.
#Hint : Import unittest module and use TestCase utility of it.
#Define a test test_isEven1, inside TestIsEvenMethod, that checks if isEven(5) returns False or not.
#Hint : Use assertEqual method to verify the function output with expected output.
#Add the statement unittest.main(), outside the class definition.

#Define another test test_isEven2, inside TestIsEvenMethod, that checks if isEven(10) returns True or not.
#Hint : Use assertEqual method to verify the function output with expected output

#Define one more test test_isEven3, inside TestIsEvenMethod, that checks if isEven function raises TypeError when a string hello is passed as argument.
#Hint : Use assertRaises
#Run the entire Test case and ensure that you pass all above three defined tests.
#Hint : Make use of unittest.main() for running the test case.

import unittest

def isEven(x):
    if isinstance(x,int):
        if x%2==0:
            return True
        else:
            return False
    else:
         raise TypeError('test')

class TestIsEvenMethod(unittest.TestCase):
    def test_isEven1(self):
        self.assertEqual(False,isEven(5))
    def test_isEven2(self):
        self.assertEqual(True,isEven(10))
    def test_isEven3(self):
        self.assertEqual(True,isEven(10))
