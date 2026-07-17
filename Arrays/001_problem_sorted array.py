"""
Problem:
Sorted Squared Array

Difficulty:
Easy

Approach:
Two Pointer

Time Complexity:
O(n)

Space Complexity:
O(n)
"""

def sorted_squared(array):
    n = len(array)
    i = 0
    j = n - 1
    result = [0] * n

    for k in reversed(range(n)):
        if array[i] ** 2 > array[j] ** 2:
            result[k] = array[i] ** 2
            i += 1
        else:
            result[k] = array[j] ** 2
            j -= 1

    return result


array = [-6, -3, -1, 4, 5, 8]
print(sorted_squared(array))