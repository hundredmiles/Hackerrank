#!/bin/python3

import math
import os
import random
import re
import sys
# import numpy as np

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    arr_sum = []
    cost_arr = [0, 0, 0, 0, 0, 0, 0, 0]

    mask = [
    [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
    [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
    [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
    [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
    [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
    [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
    [[6, 7, 2], [1, 5, 9], [8, 3, 4]]
    ]
    
    for i in range(8):
        for row in range(3):
            for counter in range(3):
                cost = abs(mask[i][row][counter] - s[row][counter])
                cost_arr[i] += cost
    return min(cost_arr)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
