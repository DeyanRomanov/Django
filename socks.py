import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    couple = 0
    while ar:
        s = ar[0]
        if ar.count(s) // 2 > 0:
            couple += (ar.count(s) // 2)
        while s in ar:
            ar.remove(s)
    return couple


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
