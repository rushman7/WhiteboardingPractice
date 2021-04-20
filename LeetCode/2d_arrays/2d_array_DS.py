#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    result = float('-inf')
    
    for i in range(1, len(arr)-1):
        for j in range(1, len(arr[i])-1):
            curr_glass = curr_hourglass_sum(i, j, arr)
            result = max(curr_glass, result)
    
    return result
            
def curr_hourglass_sum(i, j, arr):
    directions = [(-1,-1),(-1,0),(-1,1),(1,1),(1,0),(1,-1)]
    _sum = arr[i][j]
    
    for x, y in directions:
        _sum += (arr[i+x][j+y])
    
    return _sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
