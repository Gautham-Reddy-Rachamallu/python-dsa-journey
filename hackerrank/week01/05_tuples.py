"""
HackerRank - Tuples
Chapter 4 concept: tuples (immutability), .split(), generator expression
wrapped in tuple()
Date: Sep 15, 2026

Task:
Given n, then a line of n space-separated integers, build a tuple T
from those integers and print hash(T).

Note: hash() need not be imported - it's a built-in.
Important: the exact numeric hash value can differ across Python
versions / 32-bit vs 64-bit systems / environments - this is a known
quirk of hash(), not a bug. What matters is the LOGIC: build a real
tuple, then hash it and print it. HackerRank's grader checks logic,
not an exact match to the sample number.

Bugs caught and fixed this session:
1. First attempt did `for i in n:` - but n is just the single count
   (e.g. 2), not a collection to loop over. The actual integers live
   on a SEPARATE second input() line that was never read.
2. Tried `n.split()` - .split() only works on strings, and n is an
   int (also the wrong line to split anyway).
3. Tried `t.append(space)` - tuples are immutable, they have no
   .append() method (same lesson as Chapter 4: TypeError on item
   assignment).
4. `hash(t)` called on its own line with no print() - same lesson as
   Problem 1 (Print Function): a function's result is thrown away
   unless printed or stored.
5. `t = (int(v) for v in values)` - parentheses alone do NOT make a
   tuple; that syntax creates a GENERATOR expression instead (a lazy
   object). Confirmed by testing: hashing it gave a small, meaningless
   number based on memory location, not the tuple's actual contents.
   Fixed by wrapping it in the tuple() function call: tuple(int(v)
   for v in values).

Test verified: correct tuple is built and hashed (confirmed by
printing t and testing with multiple inputs); exact hash number
varies by environment as expected.
"""

n = int(input())
values = input().split()
t = tuple(int(v) for v in values)
print(hash(t))
