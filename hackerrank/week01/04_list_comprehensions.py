"""
HackerRank - List Comprehensions
Chapter 4 concept: nested list comprehensions (multiple for clauses +
an if condition, all inside one set of brackets)
Date: Sep 15, 2026

Task:
Given integers x, y, z (cuboid dimensions) and n, print a list of all
coordinates [i, j, k] with 0 <= i <= x, 0 <= j <= y, 0 <= k <= z, such
that i + j + k != n. Must use a list comprehension, not nested loops,
as a learning exercise. Output in lexicographic order.

Sample Input:
1
1
1
2

Sample Output:
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

Progression this session:
1. First attempt solved it correctly but with 3 nested for-loops and
   .append() - same output as required, but not what the problem is
   testing (explicitly asks for a list comprehension, and the nested-
   loop version wastes a throwaway `coordinates = []` list every
   single iteration).
2. First comprehension attempt had the for-clauses in the right order
   but was MISSING the `if i+j+k != n` filter entirely, so it printed
   every combination (8 items) instead of only the valid ones (5 items).
3. Fixed by adding `if i+j+k != n` at the very end, after all three
   for clauses - confirmed the general rule: in a comprehension, `for`
   clauses come first (in nesting order), then the `if` filter last.

Test verified against sample I/O - output matches exactly.
"""

x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print(result)
