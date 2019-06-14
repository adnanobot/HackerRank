"""
    Day 7 of 30 days of coding from hackerrank.com : Let's review

    author : adnanobot

    Arrays
    conditions : size of array : 1 <= N <= 1000
                 value of the element of the array : 1 <= N <= 10000
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def print_reverse(arr, n):
    for i in range(1, n+1):
      print(str(arr[n-i]), end = " ")

if __name__ == '__main__':
    print("please enter the size of the array: ")
    n = int(input())

    # check the validity of the array size 1 <= N <= 1000
    if (n >= 1 and n <= 1000) is False:
        print("[Error] Invalid input")
    else:
        print("please enter the elements of the array: ")
        arr = list(map(int, input().rstrip().split()))
        print("original array: ", arr)

        # print the array in reverse order
        print_reverse(arr, n)
