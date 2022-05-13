#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    valley = 0
    start_to_down = False
    sea = 0
    for s in path:
        if s == 'D':
            sea -= 1
        else:
            sea += 1
        if sea < 0:
            start_to_down = True
        if start_to_down is True and sea == 0:
            valley += 1
            start_to_down = False
    return valley


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()


