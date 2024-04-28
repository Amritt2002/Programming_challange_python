# Coding Exercise - Python : Sorted Squared Array
# Question

# You are given an array of Integers in which each subsequent value is not less than the previous value. Write a function that takes this array as an input and returns a new array with the squares of each number sorted in ascending order.

# Remember

# You can solve this question in multiple ways.

# Think about the following -

# 1.What would be the brute force way of solving this question ? What would be the Time and Space complexity of this approach?

# 2.Is there a better way to solve this with a more optimum Time complexity than the Brute force way ? 

Solution:
def sorted_squared(arr):
    # Square each element in the input array
    squared_values = [x**2 for x in arr]
    
    # Sort the squared values in ascending order
    sorted_squares = sorted(squared_values)


#Brute force method
# Time = O(nlogn)  Space = O(n)
def sorted_squared(array):
    new_array = [0]*len(array)
    for i in range(len(array)):
        new_array[i] = array[i]**2
        # new_array[i] = array[i]*array[i]
    new_array.sort()
    return new_array
#def square_and_sort(arr):
#    return sorted([num**2 for num in arr])
    
# Time = O(n) Space = O(n)
def sorted_squared(array):
    i = 0
    j = len(array) - 1
    new_array = [0] * len(array)
    for k in reversed(range(len(array))):
        sq_i = array[i]**2
        sq_j = array[j]** 2
        if sq_i > sq_j:
            new_array[k] = sq_i
            i += 1
        else:
            new_array[k] = sq_j
            j -= 1
    return new_array    
