"""
    Day 7 of 30 days of coding from hackerrank.com : Let's review

    author : adnanobot

    Arrays
    conditions : size of array : 1 <= N <= 1000
                 value of the element of the array : 1 <= N <= 10000
"""

arr =[[-1, -1, 0, -9, -2, -2],
     [-2, -1, -6, -8, -2, -5],
     [-1, -1, -1, -2, -3, -4],
     [-1, -9, -2, -4, -4, -5],
     [-7, -3, -3, -2, -9, -9],
     [-1, -3, -1, -2, -4, -5]]

sum = 0
sums = []
for i in range(0, 4):
  for j in range(0, 4):
    for k in range(j, j+3):
      sum += arr[i][k] + arr[i+2][k]

    sum += arr[i+1][j+1] #adding the center of the hour glass
    print("sum: ", sum)
    sums.append(sum)
    sum = 0

print("maximum sum is: ", max(sums))
