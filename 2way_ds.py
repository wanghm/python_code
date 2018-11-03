#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_val = -64
    for cur_row in range(4):
        for cur_col in range(4):
            cur_val = \
                arr[cur_row][cur_col] + arr[cur_row][cur_col + 1] + arr[cur_row][cur_col + 2] + \
                arr[cur_row + 1][cur_col + 1] + \
                arr[cur_row + 2][cur_col] + arr[cur_row + 2][cur_col + 1] + \
                arr[cur_row + 2][cur_col + 2]

            if max_val <  cur_val:
                max_val = cur_val

    return max_val
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
