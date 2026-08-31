# Chapter 3 - Lists (Revision Notes)

*Covered: Aug 31, 2026 | Code: `code/week01/lists.py` | Status: Done*

Read this in 2 minutes any time you need to refresh Chapter 3 without re-reading the whole book chapter or re-running code.

## Core facts

| Concept | Rule | Example |
|---|---|---|
| Indexing | Starts at **0**, not 1 | `colours[0]` -> first item |
| Negative indexing | Counts from the end, `-1` = last | `colours[-1]` -> last item |
| `len(list)` | Returns the count of items | `len([1,2,3])` -> `3` |
| `.append(x)` | Adds `x` to the **end** | O(1) - instant |
| `.insert(i, x)` | Inserts `x` at position `i`, shifts rest right | O(n) worst case |
| `.remove(value)` | Deletes the **first match by value**; errors if missing | O(n) - has to search |
| `.pop()` | Removes + **returns** the **last** item | O(1) - instant |
| `.pop(i)` | Removes + returns item at index `i` | O(n) if `i` isn't near the end - everything after shifts left |
| `.sort()` | Sorts the list **permanently**, in place | changes the original |
| `sorted(list)` | Returns a **new** sorted list | original list untouched |
| `list[start:stop]` | Slice: includes `start`, **excludes** `stop` | `nums[1:4]` -> indexes 1,2,3 |
| `list[:n]` | From the beginning up to (not including) `n` | |
| `list[n:]` | From index `n` to the end | |

## The one that trips everyone up: copying

```python
original = [1, 2, 3]
same_list = original       # NOT a copy - both names point at the SAME list
real_copy = original[:]    # a full slice - an actual INDEPENDENT copy
```

If you mutate `same_list`, `original` changes too. If you mutate `real_copy`, `original` is untouched.
This is the same underlying idea as the baseline assessment question about `y = x; y.append(4)`.

## Mistake made + fixed this session (worth re-reading)

Asked to remove the **first** item with `.pop()`, first attempt used `num.pop()` with no argument -
which removes the **last** item by default, not the first. Fix: `num.pop(0)`.

**Why this matters for DSA later:** `.pop()` (last item) is O(1). `.pop(0)` (first item) is O(n),
because Python has to shift every remaining element one position left to close the gap. Popping from
the front of a Python list repeatedly in a loop is a classic beginner performance mistake - if you
need fast removals from both ends, that's what a `collections.deque` is for (we'll hit this in DSA).

## Quick self-test (cover the table above and answer these)

1. What does `colours[-2]` return in `["red", "blue", "green", "purple"]`?
2. What's the time complexity difference between `.pop()` and `.pop(0)`, and why?
3. Does `.sort()` return a new list or change the original?
4. `y = x` vs `y = x[:]` - which one is a real copy?
5. What does `nums[2:]` return from `[10, 20, 30, 40, 50]`?

*(Answers: 1. 'blue' | 2. pop() is O(1) instant, pop(0) is O(n) because everything shifts left | 3. changes the original, in place | 4. `x[:]` is the real copy | 5. `[30, 40, 50]`)*
