"""
 Day 3 of 30 days of coding challenge from hackerrank.com
 --------------------------------------------------------
 Objective :
 In this challenge, we're getting started with conditional statements.
 Task:
 Given an integer, n , perform the following conditional actions:
 if 2 < n <= 5
 if 6 < n <= 20: weird
 if n > 20 : not weird

 Constraints: 1 <= n <= 100
 Output Format: Print Weird if the number is weird; otherwise, print Not Weird.
"""

import math
import os
import random
import re
import sys

def checker(n):
    # chekc if it is even
    if n >= 1 and n <= 100:
        if (n % 2) == 0:
            # if 2 < n <= 5: not weird
            if n > 2 and n <= 5:
                print("Not Weird")
            # if 6 < n <= 20: weird
            if n > 6 and n <= 20:
                print("Weird")
            # if n > 20 : not weird
            if n > 20:
                print("Not Weird")

        # else : print weird
        else:
            print("Weird")


if __name__ == '__main__':
    print("please enter an integer: ")
    N = int(input())
    checker(N)
