"""
    day 5 of 30 days of coding from hackerrank.com

    author : adnanobot
    
    Task:
    Given an integer -n, print its first multiples.
    Each multiple n * i (where 1 <= i <= 10) should be printed on a new line in the form: n x i = result.

    Input Format:
    A single integer: n.

    Constraints: 2 <= n <= 20

    Output Format:
    Print 10 lines of output;
    each line i (where 1 <= i <= 10) contains the result of n * i in the form:
    n x i = result.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def check_validity(n):
    if n >= 2 and n <= 20:
        validity = True
    else:
        validity = False
    return validity

def multiply(n):
    for i in range(1, 11):
        print("%d x %d = %d" % (n, i, n*i))

if __name__ == '__main__':
    print("Please enter n: (2 <= n <= 20)")
    n = int(input())
    valid = check_validity(n)
    if valid:
        multiply(n)
