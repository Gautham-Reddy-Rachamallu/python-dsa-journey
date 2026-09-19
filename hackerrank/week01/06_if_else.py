"""
HackerRank - Python If-Else
https://www.hackerrank.com/challenges/py-if-else/problem
Chapter 5 concepts: if/elif/else, comparison operators, and, in (range
membership)
Date: Sep 17, 2026

Task:
Given an integer n:
- If n is odd, print "Weird"
- If n is even and in the inclusive range 2 to 5, print "Not Weird"
- If n is even and in the inclusive range 6 to 20, print "Weird"
- If n is even and greater than 20, print "Not Weird"

Sample Input 0: 3   -> Sample Output 0: Weird
Sample Input 1: 24  -> Sample Output 1: Not Weird

Bugs caught and fixed this session:
1. First attempt wrote `n%2==0 and range(2,6)` with NO `in` keyword.
   A bare range object is always truthy regardless of n's value, so
   this condition was really just checking "is n even" - it never
   actually tested whether n fell inside the range at all. This made
   every even number fall into the SECOND branch no matter what.
   Caught by manually testing n=10 (even, should be in 6-20 -> Weird)
   and getting "Not Weird" instead - proved the range check wasn't
   really happening.
   Fixed by adding `in`: `n%2==0 and n in range(2,6)`.
2. Typo: "Weired" instead of "Weird" in one branch - would have
   failed exact-match grading on HackerRank even after the logic fix.

Test verified with three inputs after fixes:
  n=3  -> Weird
  n=24 -> Not Weird
  n=10 -> Weird
(all match expected output)
"""

n = int(input())

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and n in range(2, 6):
    print("Not Weird")
elif n % 2 == 0 and n in range(6, 21):
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")
