"""
Week 1 - Chapter 3: Introducing Lists
Python Crash Course - Chapter 3
Date: Aug 31, 2026

Covers: indexing, negative indexing, len(), append(), insert(), remove(),
pop(), sort() vs sorted(), slicing, and copying (reference vs real copy).
Read top to bottom for a full revision of Chapter 3 in ~5 minutes.
"""

# ============================================================
# 1. LISTS INTRO - creating a list, indexing, len(), append()
# ============================================================
# A list holds multiple values in order, and can be changed after creation.
# Python indexing starts at 0, not 1.

colour = ["red", "blue", "green"]

print(colour[0])   # red   -> index 0 calls the first element
print(colour[-1])  # green -> negative indexes count from the end; -1 is the last element
print(colour[-2])  # blue  -> -2 is the second-to-last element

colour.append("purple")   # append() adds a new element at the END of the list
print(colour)              # ['red', 'blue', 'green', 'purple']

print(len(colour))         # len() tells you how many elements are in the list -> 4


# --- practice: same ideas, different list ---
colours = ["red", "green", "blue", "yellow"]
print(f"the third colour is {colours[2]} \nthe last colour is {colours[-1]}")
colours.append("purple")
print(colours)
print(f"there are {len(colours)} colours.")


# ============================================================
# 2. INSERT, REMOVE, POP, SORT
# ============================================================
# .insert(index, item) -> puts item at a specific position, shifts the rest right
# .remove(value)       -> finds the FIRST matching value and deletes it (error if not found)
# .pop()                -> removes AND RETURNS the last item (or a given index)
# .sort()               -> changes the list permanently
# sorted(list)          -> returns a NEW sorted list, original stays untouched

nums = [4, 1, 3, 2]
nums.insert(2, 99)      # [4, 1, 99, 3, 2] -> 99 inserted at index 2
print(nums)
nums.remove(3)          # removes the value 3 (not index 3)
print(nums)
last = nums.pop()       # removes + returns the LAST item
print(last, nums)
nums.sort()             # sorts nums permanently, in place
print(nums)
nums.append(0)
sorted(nums)            # NOTE: this line does nothing on its own - the result
                        # is thrown away unless you print() it or store it.
print(nums, sorted(nums))


# --- practice: insert/remove/pop combined ---
num = [5, 2, 9, 1, 7]
num.insert(2, 100)        # [5, 2, 100, 9, 1, 7]
print(num)
num.remove(9)              # remove BY VALUE -> [5, 2, 100, 1, 7]
print(num)

# IMPORTANT DISTINCTION (this was the one real bug of the session):
# num.pop()   -> removes the LAST item  -> O(1), instant regardless of list size
# num.pop(0)  -> removes the FIRST item -> O(n), every remaining item shifts left
last = num.pop(0)
print(f"removed: {last} and the list is: {num}")
print(f"{sorted(num)} and the original is {num}")   # sorted(num) doesn't touch num


# ============================================================
# 3. SLICING AND COPYING LISTS
# ============================================================
# Slicing: list[start:stop] includes start, EXCLUDES stop.
# Leave start or stop empty to mean "from the beginning" / "to the end".

nums = [10, 20, 30, 40, 50]
print(nums[1:4])   # [20, 30, 40] -> starts at index 1, stops BEFORE index 4
print(nums[:2])    # [10, 20]     -> from the start, stops before index 2
print(nums[2:])    # [30, 40, 50] -> from index 2 to the end

# Copying: y = x does NOT make a real copy - y just points at the SAME list.
# y = x[:] (a full slice) makes an independent, real copy.

original = [1, 2, 3]
same_list = original       # NOT a copy - points at the same list as original
real_copy = original[:]    # an actual independent copy

same_list.append(4)
real_copy.append(99)

print(original)    # [1, 2, 3, 4]  -> changed! same_list was never a separate list
print(real_copy)   # [1, 2, 3, 99] -> original list untouched


# --- practice: slicing + reference vs real copy, side by side ---
nums = [10, 20, 30, 40, 50]
print(nums[1:4])   # [20, 30, 40] -> the middle three values
print(nums[:2])    # [10, 20]     -> first two values
print(nums[3:])    # [40, 50]     -> last two values

original = ["a", "b", "c"]
fake_copy = original       # same list, two names
real_copy = original[:]    # true independent copy
fake_copy.append("z")
real_copy.append("y")
print(original)     # ['a', 'b', 'c', 'z']  -> changed via fake_copy
print(fake_copy)    # ['a', 'b', 'c', 'z']  -> same list as original
print(real_copy)    # ['a', 'b', 'c', 'y']  -> independent, only this one has 'y'


# ============================================================
# KEY TAKEAWAYS (revise these before moving to Chapter 4)
# ============================================================
# - Indexing starts at 0. Negative indexes count from the end (-1 = last).
# - .append(), indexing, and .pop() (no args) are all O(1) - instant.
# - .pop(0) and .remove() are O(n) - they can require shifting every element.
# - .sort() changes the list permanently; sorted() returns a new list and
#   leaves the original alone.
# - slice[start:stop] excludes stop.
# - `y = x` makes y point at the SAME list. `y = x[:]` makes a real, independent copy.
