#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here


numberOfSwaps = 0
for i in range(n):
    # Track number of elements swapped during a single array traversal
    
    for j in  range(n-1):
        # Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]):
            a[j], a[j + 1] = a[j + 1], a[j]
            numberOfSwaps += 1
    
    # If no elements were swapped during a traversal, array is sorted
    #if (numberOfSwaps == 0):
    #    break

print("Array is sorted in " + str(numberOfSwaps) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a.pop()))

