"""　
g = G
o = O = 0 = () = [] = <>
l = L = I
e = E = 3
"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    string = input()

    # Create your code here
    pattern='(G|g)(O|o|0|<>|\(\)|\[\]){2}(G|g)(L|l|I)(E|e|3)$'

    if re.match(pattern, string) is None:
        print('False')
    else:
        print('True')
        
