"""
Week 1 - Chapter 4: Working with Lists (loops, range, comprehensions, tuples)
Python Crash Course - Chapter 4
Date: Sep 1-2, 2026

Covers: for loops over lists, range() + numerical lists, min()/max()/sum(),
list comprehensions, and tuples (immutability).
Read top to bottom for a full revision of Chapter 4 in ~5 minutes.
"""

# ============================================================
# 1. FOR LOOPS OVER LISTS
# ============================================================
# A for loop hands you each item in a list, one at a time, automatically.
# No indexing needed - Python does the counting for you.

fruits = ["apple", "banana", "cherry", "mango"]
for fruit in fruits:
    print(f"i want to eat a {fruit}")

# IMPORTANT DISTINCTION (caught and understood this session):
# fruits  -> the whole list. print(fruits) prints it once, as one object.
# fruit   -> the LOOP VARIABLE. Only exists inside the loop, holds ONE item
#            at a time, gets overwritten each repeat. print(fruit) inside the
#            loop runs once PER ITEM, one per line.
# The names "fruit"/"fruits" are just a readability convention (singular for
# the loop variable, plural for the list) - Python doesn't enforce this.
# `for x in fruits:` would work identically, just less readable.


# --- filtering pattern: loop + if, keep only what matches ---
nums = [3, 7, 1, 9, 4]
for x in nums:
    if x > 4:
        print(x)          # 7, 9

evens = []
nums = [1, 2, 3, 4, 5, 6, 7, 8]
for x in nums:
    if x % 2 == 0:
        evens.append(x)
print(evens)               # [2, 4, 6, 8]


# ============================================================
# 2. RANGE() AND NUMERICAL LISTS
# ============================================================
# range(start, stop) generates numbers from start up to (NOT including) stop.
# Same "excludes the end" rule as list slicing.

for x in range(1, 21):
    print(x)                # prints 1 through 20

cubes = []
for i in range(1, 11):
    cubes.append(i ** 3)
print(cubes)                 # [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# built-ins for numerical lists: min(), max(), sum()
scores = [67, 88, 45, 90, 72, 100, 58]
print(min(scores), max(scores), sum(scores))          # 45 100 520
print(f"the avg is {sum(scores) / len(scores)}")        # 74.28571428571429

# direct real-world unlock: HackerRank "Print Function"
# print n numbers from 1 to n with NO spaces/newlines between them
n = 9
for i in range(1, n + 1):
    print(i, end="")        # 123456789


# ============================================================
# 3. LIST COMPREHENSIONS
# ============================================================
# Shorthand for the "make empty list -> loop -> append" pattern used above.
# result = [<expression> for x in something]
# result = [<expression> for x in something if <condition>]   (with filter)

# the long way (what section 1 & 2 used)
cubes = []
for i in range(1, 11):
    cubes.append(i ** 3)

# the comprehension way - identical result, one line
cubes = [i ** 3 for i in range(1, 11)]
print(cubes)                 # [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

nums = [1, 2, 3, 4, 5, 6, 7, 8]
evens = [x for x in nums if x % 2 == 0]
print(evens)                  # [2, 4, 6, 8]

words = ["hi", "hello", "hey", "greetings", "sup"]
lengths = [len(w) for w in words]
print(lengths)                 # [2, 5, 3, 10, 3]

nums = [12, 7, 18, 3, 25, 9, 30]
more_10 = [x for x in nums if x > 10]
print(more_10)                  # [12, 18, 25, 30]

# BUG CAUGHT THIS SESSION (real, worth remembering):
# Typed `even = [...]` then `print(evens)` - a typo, different variable names.
# This did NOT crash, because a leftover `evens` from an earlier cell already
# existed in memory (Jupyter/notebooks keep ALL variables alive across cells,
# in the order cells are RUN, not the order they appear on the page).
# Lesson: a typo that accidentally matches an old variable name won't error -
# it silently gives you STALE, WRONG data. Always double check variable names
# match exactly, especially in notebooks where old state lingers.


# ============================================================
# 4. TUPLES
# ============================================================
# Like a list, but IMMUTABLE - once created, items cannot be changed, added,
# or removed. Written with () instead of []. Reading works identically to
# lists: indexing, negative indexing, slicing, looping.

rgb = (255, 0, 128)
print(rgb[0], rgb[1], rgb[2])    # 255 0 128

for value in rgb:                 # direct iteration - preferred over
    print(value)                  # range(len(rgb)) style indexing when you
                                   # don't need the position itself

# rgb[0] = 10   -> TypeError: 'tuple' object does not support item assignment
# This is Python deliberately REFUSING the operation, by design - not a bug.
# It proves tuples cannot be changed/added to/removed from after creation.

# the only way to "change" a tuple: replace the WHOLE variable with a new one
size = (10, 20)
print(size)          # (10, 20)
size = (15, 25)       # this is a brand new tuple, not an edit
print(size)           # (15, 25)


# ============================================================
# KEY TAKEAWAYS (revise these before moving to Chapter 5)
# ============================================================
# - `for item in list:` gives you VALUES directly. `for i in range(len(list)):`
#   gives you POSITIONS - use direct iteration unless you specifically need
#   the index (e.g. comparing list[i] to list[i+1]).
# - range(start, stop) excludes stop, same rule as slicing.
# - min(), max(), sum() work directly on lists of numbers.
# - List comprehensions `[expr for x in iterable if condition]` are shorthand
#   for the "empty list -> loop -> append" pattern - not a new concept.
# - Tuples are immutable: use () instead of []. Reading works like lists;
#   writing to an index raises TypeError by design.
# - Notebooks keep every variable alive across ALL cells run so far - a typo
#   matching an old variable name will silently use STALE data instead of
#   crashing. Always sanity-check variable names match exactly.
