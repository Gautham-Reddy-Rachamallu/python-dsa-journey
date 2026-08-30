# Baseline Assessment

**Taken:** Aug 30, 2026. Result: near-zero prior Python knowledge confirmed — correct and expected
starting point; this is what put us at true Chapter 1 pace.

---

## Part A — Conceptual (10 questions)

1. What is the difference between a `list` and a `tuple` in Python?
2. What does the following print, and why?
   ```python
   x = [1, 2, 3]
   y = x
   y.append(4)
   print(x)
   ```
3. What is the difference between `==` and `is`?
4. What does `*args` do in a function definition? Give a one-line example.
5. What is a dictionary, and what must a dictionary key be (and not be)?
6. What is the output of `range(2, 10, 3)` if converted to a list?
7. What's the difference between `append()` and `extend()` on a list?
8. What does `try`/`except`/`finally` do, and when does `finally` run?
9. What is a class, and what is `self` inside a class method?
10. What is the difference between a function that uses `return` and one that only uses `print()`?

## Part B — Small Coding Problems

1. Write a function `is_even(n)` that returns `True` if `n` is even, else `False`.
2. Write a function `reverse_string(s)` that returns the reverse of a string **without using `s[::-1]`**.
3. Given a list of numbers, return a new list containing only the numbers greater than 10.
4. Write a function `count_vowels(s)` that returns how many vowels are in a string.
5. Given a dictionary of `{name: score}`, print the name with the highest score.

## Part C — Debugging

**Debug 1:**
```python
def add_to_list(item, my_list=[]):
    my_list.append(item)
    return my_list

print(add_to_list(1))
print(add_to_list(2))
```

**Debug 2:**
```python
def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    average = total / len(numbers)
    return average

scores = []
print(calculate_average(scores))
```

## Part D — Problem-Solving Challenge

```
Input: [4, 3, 4, 4, 4, 5, 5, 3, 3]
```
Find the number(s) that appear an odd number of times, and describe the approach's rough speed.

---

## Outcome

All answers were "don't know" or incorrect guesses — confirmed a true zero-background start.
This is not a negative result; it's exactly what Chapter 1 of the textbook is built for, and it
set the calibration for Week 1's pace (see `03_roadmap.md`).
