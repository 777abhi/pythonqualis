import numpy as np
import statistics as st

normal_array = np.array([9.2,10.7,6.8,9,3.4,5.7,5.7])

print(normal_array)

#Calculate Mean, Median, Standard Deviation and Variance with the built-in functions of Numpy Packag

mean = np.mean(normal_array)
median = np.median(normal_array)
sd = np.std(normal_array)
variance = np.var(normal_array)

#Calculate Mode with the built-in function of Statistics Package.
#(Calculation of mode must print the value which has the greatest number of occurrences in the array)
mode = st.mode(normal_array)

#Display the output in the following order
#Mean
#Median
#Standard Deviation
#Variance
#Mode
print(mean)
print(median)
print(sd)
print(variance)
print(mode)

def test_sample():
    assert 2 == 2

from test_co2 import TestIsEvenMethod