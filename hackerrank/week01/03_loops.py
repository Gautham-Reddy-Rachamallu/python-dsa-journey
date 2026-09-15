"""
HackerRank - Loops
Chapter 4 concepts: int(input()), for loop with range(), ** operator
Date: Sep 15, 2026

Task:
Given a non-negative integer n, print the square of each integer from
0 to n-1, each on its own line.

Sample Input:
5

Sample Output:
0
1
4
9
16

Note: added an n < 0 guard as a bonus defensive check (not required by
the problem, since n is guaranteed non-negative, but good habit).

Test verified against sample I/O - output matches exactly.
"""

n = int(input())

if n < 0:
    print("pls use a +ve number ")
else:
    for i in range(n):  # range(n) same as range(0, n)
        i = i ** 2
        print(i)
