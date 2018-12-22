#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level = [0]           # level in each step
    sea_level = [0]    #index of the steps where Gary is in sea leval

    steps = list(s)
 
    num_sea_level = 1
    for i  in range(len(steps)):
        if steps[i] == "U":
            level.append(level[len(level) -1] + 1)
        elif steps[i] == "D":
            level.append(level[len(level) -1] - 1)
        else:
            raise exception

        if level[len(level) -1] == 0:
            sea_level.append(len(level) -1)
    

    print("steps: " + str(steps))

    print("level: " + str(level))
    print("sea_level:" + str(sea_level))

    ret = 0
    for x in range(len(sea_level) - 1):
        print("sea_level[x+1] = " + str(sea_level[x+1] ))
        if level[sea_level[x+1] -1] < 0:
            ret += 1
        print("ret=" + str(ret))
    
    return ret


        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
