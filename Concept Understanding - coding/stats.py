"""
# mean is the average of the values, it can be positive, negative and zero also.

import statistics

li = [1, 2, 36, 1, 4, 56, 70, 2, 2, 4, 6]

print(statistics.mean(li))

"""
# -------------------------------------------------------------------------------------

"""
# median means to find the middle entries of the sorted series/data.
# sorting will be done in the beginning.
# median_low() and median_high() functions provide the low and high entries of the median.

import statistics

from fractions import Fraction as fr

# tuple of positive integer numbers
data1 = (2, 3, 4, 5, 7, 9, 11)
 
# tuple of floating point values
data2 = (2.4, 5.1, 6.7, 8.9)
 
# tuple of fractional numbers
data3 = (fr(1, 2), fr(44, 12),
        fr(10, 3), fr(2, 3))
 
# tuple of a set of negative integers
data4 = (-5, -1, -12, -19, -3)
 
# tuple of set of positive
# and negative integers
data5 = (-1, -2, -3, -4, 4, 3, 2, 1)

print(statistics.median(data1))
print(statistics.median(data2))
print(statistics.median(data3))
print(statistics.median(data4))
print(statistics.median(data5))

"""
# -----------------------------------------------------------------------------------

"""
# mode: finding the entry which has got maximum number of occurences/frequency.

import statistics
from fractions import Fraction as fr

# tuple of positive integer numbers
data1 = (2, 3, 3, 4, 5, 5, 5, 5, 6, 6, 6, 7)
 
# tuple of a set of floating point values
data2 = (2.4, 1.3, 1.3, 1.3, 2.4, 4.6)
 
# tuple of a set of fractional numbers
data3 = (fr(1, 2), fr(1, 2), fr(10, 3), fr(2, 3))
 
# tuple of a set of negative integers
data4 = (-1, -2, -2, -2, -7, -7, -9)
 
# tuple of strings
data5 = ("red", "blue", "black", "blue", "black", "black", "brown")

print(statistics.mode(data1))
print(statistics.mode(data2))
print(statistics.mode(data3))
print(statistics.mode(data4))
print(statistics.mode(data5))

"""
# -----------------------------------------------------------------------------------------------------

"""
# variance is the average squared deviation from the mean.
# (sum of all the differences with mean)**2/n.
# standard deviation is the square root of variance.


import statistics
sample1 = (1, 2, 5, 4, 8, 9, 12)
sample2 = (-2, -4, -3, -1, -5, -6)
print(statistics.variance(sample2))

def mean_returner(data):
    no_of_items = 0
    sum = 0
    for item in data:
        no_of_items = no_of_items + 1
        sum = sum + item
    mean = sum/no_of_items
    return mean

def variance_returner(data):
    mean = mean_returner(data)
    sum = 0
    number_of_items = 0
    for item in data:
        sum = sum + (item - mean)**2
        number_of_items = number_of_items + 1
    variance = sum/number_of_items
    return variance


variance = variance_returner(sample2)
print(variance)
"""

# --------------------------------------------------------------------------------------------------------------------
