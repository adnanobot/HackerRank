"""
    HackerRank : Day 10 Binary Numbers
    * Convert the given input number into decimal
    * Count the max no of consecutive 1 in the binary
    e.g.: 5 = 0101, max_con_one = 1
          13 = 1101, may_con_one = 2
"""

def binary(n):
    new = 0
    old = 0
    while True:
        remainder = int(n % 2)
        if remainder == 1 :
            new += 1
        elif new > old:
            old = new
            new = 0
        else:
            new = 0

        result = int(n / 2)
        print("res, rem", result, remainder, old, new)
        if(result) != 0: n = result
        else:  break

    print("max no of conscutive ones: ", max(new, old))

if __name__ == '__main__':
  n = input("please enter an integer: ")
  binary(int(n))
