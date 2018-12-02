#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    l_str = list(format(n, '08b'))

    max_consecutive_1 = 0
    consecutive_1 = 0

    for i in range(len(l_str)):
        if l_str[i] == '1':
            consecutive_1 += 1
            if max_consecutive_1 < consecutive_1:
                max_consecutive_1 = consecutive_1
        else:
            consecutive_1 = 0

    print(max_consecutive_1)
