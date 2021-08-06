"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

# reference from https://github.com/VineetPrasadVerma/Udacity-DataStructures-And-Algorithms-In-Python/blob/master/BinarySearch.py


def binary_search(input_array, value):

    result = input_array
    while len(input_array) >= 1:

        listSize = len(input_array)

        if (listSize % 2) != 0:
            midElement = input_array[int(listSize/2)]
        else:
            midElement = input_array[int((listSize/2)-1)]

        if value == midElement:
            return result.index(midElement)
        elif value < midElement:
            input_array = input_array[:(input_array.index(midElement))]
        elif value > midElement:
            input_array = input_array[(input_array.index(midElement)+1):]

    return -1
