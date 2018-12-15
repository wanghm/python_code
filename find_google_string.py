"""　
g = G
o = O = 0 = () = [] = <>
l = L = I
e = E = 3
https://regexper.com/#%28G%7Cg%29%28O%7Co%7C0%7C%3C%3E%7C%5C%28%5C%29%7C%5C%5B%5C%5D%29%7B2%7D%28G%7Cg%29%28L%7Cl%7CI%29%28E%7Ce%7C3%29
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
        
