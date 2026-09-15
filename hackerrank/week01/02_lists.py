"""
HackerRank - Lists
Chapter 3-4 concepts: input(), int(), list methods, for loop, if/elif,
and .split() (string -> list of words, taught this session as the one
gap between prior chapters and this problem).
Date: Sep 15, 2026

Task:
Start with an empty list. Read N, then N command lines. Each line is
one of: insert i e / remove e / append e / sort / pop / reverse / print.
Perform the command; "print" prints the current list.

Key concept - .split():
  line = "insert 0 5"
  parts = line.split()      # ['insert', '0', '5'] - breaks string on spaces
  parts[0] is the command name; parts[1]/parts[2] are STILL STRINGS,
  so they need int() before being used as index/value.

Bug caught and fixed this session:
  First attempt had branches for insert/print/remove/append/pop/reverse
  but was MISSING an elif branch for "sort" entirely - so the sort
  command silently did nothing (no error, because it just fell through
  the whole if/elif chain with no match). Caught by comparing actual
  output [5, 10, 9, 1] against expected [1, 5, 9, 10] and manually
  tracing which command in the input had no matching branch.
  Fixed by adding the missing elif command == "sort": my_list.sort()

Test verified against sample I/O - all three print statements match:
  [6, 5, 10]
  [1, 5, 9, 10]
  [9, 5, 1]
"""

n = int(input())
my_list = []

for i in range(n):
    parts = input().split()
    command = parts[0]

    if command == "insert":
        idx = int(parts[1])
        e = int(parts[2])
        my_list.insert(idx, e)
    elif command == "print":
        print(my_list)
    elif command == "remove":
        e = int(parts[1])
        my_list.remove(e)
    elif command == "append":
        e = int(parts[1])
        my_list.append(e)
    elif command == "pop":
        my_list.pop()
    elif command == "reverse":
        my_list.reverse()
    elif command == "sort":
        my_list.sort()
