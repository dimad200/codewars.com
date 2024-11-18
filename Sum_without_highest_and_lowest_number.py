# Task
# Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).
#
# The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.
#
# Mind the input validation.

# Example
# { 6, 2, 1, 8, 10 } => 16
# { 1, 1, 11, 2, 3 } => 6
# Input validation
# If an empty value ( null, None, Nothing, nil etc. ) is given instead of an array, or the given array is an empty list or a list with only 1 element, return 0.
from types import NoneType

def sum_array(arr):
    if type(arr)==NoneType:
            return 0
    if type(arr) == list:
        if len(arr) < 3:
            return 0
        else:
            arr = sorted(arr)
            arr = arr[1:-1:]
            summ=0

            for i in range(len(arr)):
                summ = summ + arr[i]
            return summ
a=[6, 2, 1, 8, 10]
print(sum_array(a))

