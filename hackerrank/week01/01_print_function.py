"""
HackerRank - Print Function
Chapter 4 concepts: input(), int() conversion, range(), print(end="")
Date: Sep 15, 2026

Task:
Given an integer n, print integers from 1 to n as a single string with
no spaces, without building a formatted string manually.

Key bug caught and fixed this session:
1. input() ALWAYS returns a string, even if the user types a number.
   So n = input() makes n = "3" (str), not 3 (int).
2. range(1, n+1) needs n to be an int, or the "+1" fails with:
   TypeError: can only concatenate str (not "int") to str
3. First fix attempt used str(n) instead of int(n) - wrong direction
   (str -> str does nothing useful here; we need str -> int).
4. Even after picking the right function, calling int(n) on its own
   line without storing it back (n = int(n)) does nothing permanent -
   same lesson as return vs print(): a function's result must be
   CAUGHT with "=" or it's thrown away.

Fix: n = int(input())  -- convert immediately, store it back into n.

Test cases (verified against sample I/O):
  Input: 3  -> Output: 123
  Input: 9  -> Output: 123456789
"""

n = int(input())
for x in range(1, n + 1):
    print(x, end="")
