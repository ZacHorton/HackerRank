#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    # num of athletes
    n = int(nm[0])

    # num of columns
    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    # sort based off
    k = int(input())

    arr.sort(key = lambda arr: arr[k])
    for x in arr:
      print(*x)
    
