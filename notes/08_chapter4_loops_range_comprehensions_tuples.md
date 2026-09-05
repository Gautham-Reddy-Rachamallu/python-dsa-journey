# Chapter 4 Revision Notes: Working with Lists (loops, range, comprehensions, tuples)

*2-minute revision sheet. Self-sufficient - no need to go back to chat history.*

## 1. `for` loops over lists

```python
for item in my_list:
    # runs once PER ITEM, item takes each value in turn
```

- `my_list` (plural) = the whole list. `item` (singular) = the loop variable, one value at a time. This is a naming *convention* for readability, not a Python rule - `for x in my_list:` works identically.
- Anything indented under `for` runs once per item. Un-indented code after the loop runs once, after the loop finishes.
- Prefer `for item in my_list:` over `for i in range(len(my_list)): item = my_list[i]` unless you specifically need the index/position.

**Filtering pattern** (extremely common, shows up constantly in LeetCode/HackerRank):
```python
result = []
for x in some_list:
    if <condition>:
        result.append(x)   # or print(x), or anything else
```

## 2. `range()` and numerical lists

- `range(start, stop)` generates whole numbers from `start` up to but **not including** `stop` - same exclusion rule as list slicing `[start:stop]`.
- `range(5)` -> 0,1,2,3,4 (start defaults to 0)
- `range(1, n+1)` -> 1 through n inclusive (the `+1` is what makes it inclusive of n)
- `print(x, end="")` prints without a newline/space after - useful for concatenated output.
- Built-ins: `min(list)`, `max(list)`, `sum(list)` - no loop needed for these.
- Average = `sum(list) / len(list)`.

## 3. List comprehensions

Shorthand for "empty list -> loop -> append" - not a new concept, just compressed syntax.

```python
result = [<expression> for x in iterable]
result = [<expression> for x in iterable if <condition>]   # with filter
```

Examples:
```python
cubes = [i ** 3 for i in range(1, 11)]
evens = [x for x in nums if x % 2 == 0]
lengths = [len(w) for w in words]
```

## 4. Tuples

- Like a list but **immutable**: cannot change, add, or remove items after creation.
- Written with `()` instead of `[]`: `point = (3, 7)`
- **Reading works identically to lists**: indexing (`point[0]`), negative indexing, slicing, looping (`for v in point:`).
- **Writing fails on purpose**: `point[0] = 99` raises `TypeError: 'tuple' object does not support item assignment`. This is deliberate, not a bug - it's the whole point of a tuple.
- The only way to "change" a tuple is to replace the entire variable with a brand new tuple: `point = (99, 7)` (this is a new object, not an edit).
- Use tuples when you want to guarantee data can't be accidentally modified later (coordinates, RGB values, fixed records).

## Real bug caught this session (important - re-read if this happens again)

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8]
even = [x for x in nums if x % 2 == 0]   # defined "even" (typo, no 's')
print(evens)                              # printed "evens" - different name!
```

This did **not** crash with `NameError`, because a leftover `evens` variable from an earlier notebook cell was still alive in memory. Notebooks (Jupyter) keep every variable alive across **all cells run so far**, in the order they were *run*, not the order they appear on the page.

**Lesson:** a typo that happens to match an old variable name will not error - it will silently return **stale, wrong data**, and everything will look fine unless you check carefully. Always double-check variable names match exactly, especially when re-running cells out of order.

## Self-test (answer without looking above)

1. What does `for colour in colours:` actually mean - what does `colour` hold on each pass?
2. What does `range(1, 6)` generate? What about `range(6)`?
3. Rewrite this as a one-line comprehension: `result = []; for x in nums: result.append(x * 2)`
4. Why does `my_tuple[0] = 5` raise an error, but `my_tuple = (5, 7)` (full reassignment) does not?
5. Why is a typo like `even`/`evens` dangerous in a notebook, but usually safe (crashes immediately) in a plain `.py` script run fresh each time?

*(Answers: 1 - one item at a time, overwritten each loop. 2 - 1,2,3,4,5 and 0,1,2,3,4,5 respectively - wait, range(6) is 0-5, double check by running it yourself. 3 - `result = [x * 2 for x in nums]`. 4 - indexed assignment mutates an existing tuple which is disallowed; full reassignment just points the variable at a brand new tuple object. 5 - a fresh script has no leftover variables from previous runs, so an undefined name always raises NameError immediately; a notebook can have old variables lingering from earlier, out-of-order cell executions.)*
