# Progress Dashboard

*Last updated: Sep 1, 2026 (Day 3)*

```
Python Core (Ch. 1-11):     3 / 11 chapters        [######              ] ~27% (Ch4 in progress)
Book Try-It-Yourself done:  0 / 68  (working via live custom exercises instead)
HackerRank solved:           3 / 5 (Week 1 target ~8)
DSA topics covered:          0 / 15               [                    ] 0%
LeetCode solved:              0 / 200              [                    ] 0%
  Easy:   0 / 80
  Medium: 0 / 102
  Hard:   0 / 18
Current week:                Week 1 (Aug 30 - Sep 5)
Current day:                 Day 3
Current streak:               3 days
Weekly test average:          - (Test #1 due end of Week 1)
Days elapsed / total:         2.5 / 94
Schedule status:              AHEAD on Python chapters, BEHIND on HackerRank (3/8) and LeetCode (0/3, blocked by network). Chapter 4 (loops) starting fresh this session.
```

## Concepts confirmed solid (through live exercises, not just reading)

| Concept | Status | Evidence |
|---|---|---|
| `print()`, variables, `=` as storage not equality | Solid | Baseline Q3 misunderstood -> corrected same day |
| f-strings | Solid | Multiple correct independent uses, including unprompted `\n` usage |
| String methods `.upper()/.lower()/.title()` | Solid | Correct on first try |
| String concatenation `+` and `TypeError` (str + int) | Solid | Predicted output correctly, fix understood |
| Arithmetic operators `/ // % **` | Solid | All predictions correct |
| `return` vs `print()` | Solid (after 1 correction) | Baseline: didn't know -> wrote buggy `print`-based version -> self-corrected to `return` |
| `None` / implicit return | Solid | Explained after live bug encountered |
| Lists - indexing, negative indexing, `len()`, `.append()` | Solid | Correct first try, including working out "third item = index 2" independently |
| Lists - `.insert()`, `.remove()`, `sort()` vs `sorted()` | Solid | Correct on first try |
| Lists - `.pop()` vs `.pop(index)` | Solid (after 1 correction) | First attempt used `.pop()` with no arg when asked to remove the first item -> corrected to `.pop(0)`, O(1) vs O(n) distinction understood |
| Lists - slicing `[start:stop]` | Solid | All three slice exercises correct first try |
| Lists - reference (`y = x`) vs real copy (`y = x[:]`) | Solid | Correctly distinguished `fake_copy` vs `real_copy` behavior, matches baseline assessment Q2 insight |
| `for` loop + `range()` basics | Introduced, NOT yet verified | Given as a rushed mini-lesson to unblock 2 HackerRank problems - full Chapter 4 treatment (for-over-list, list comprehensions, tuples, simple stats) starts fresh this session |

## HackerRank Log (Week 1)

| Problem | Status | Notes |
|---|---|---|
| Say "Hello, World!" | Accepted | Score 5.00 |
| Arithmetic Operators | Accepted | 10 pts, all test cases passed |
| Python: Division | Accepted | 10 pts, correctly handled int/int -> float vs // |
| Print Function | Not yet submitted | Needs range()/end="" - unblocked by mini for-loop lesson, retry after Chapter 4 |
| Lists | Not yet submitted | Needs for-loop + if/elif chain over N commands - retry after Chapter 4 |

## LeetCode Log

| # | Problem | Status | Notes |
|---|---|---|---|
| 217 | Contains Duplicate | Blocked | LeetCode.com not loading - suspected network/ISP block. Try mobile data or different network. |
| 26 | Remove Duplicates from Sorted Array | Blocked | Same as above |
| 1 | Two Sum | Blocked | Same as above |

## Weekly Test Score Log

| Week | Test Topic | Python (20%) | Coding (20%) | Problem Solving (20%) | DSA (20%) | LeetCode (10%) | Debugging (10%) | Total /100 |
|---|---|---|---|---|---|---|---|---|
| 1 | Ch 1-3 | | | | | | | pending - due end of Week 1 |

## Weak Topics / Error Log

| Date | Topic/Concept | What went wrong | Status |
|---|---|---|---|
| Aug 30 | `==` vs `=` | Thought `==` was assignment | Resolved same day |
| Aug 30 | `return` vs `print()` | Wrote `is_even` using `print()` inside `if`, got `None` in output | Resolved same day - rewrote with `return`, confirmed True/False |
| Aug 30 | Variable naming discipline | Swapped `first_name`/`last_name` values twice | Cosmetic, watch for it |
| Aug 31 | `.pop()` vs `.pop(0)` | Used `.pop()` (removes last) when asked to remove the first item | Resolved same session - corrected to `.pop(0)`, O(1) vs O(n) explained |
| Sep 1 | Curriculum sequencing | Two HackerRank problems (Print Function, Lists) assigned before loops were taught | Caught by Gautham, acknowledged - fixed by doing proper Chapter 4 before resuming those problems |

## Revision Queue (spaced repetition)

| Concept | Date Learned | Review @ 1d | Review @ 3d | Review @ 7d | Review @ 14d |
|---|---|---|---|---|---|
| `return` vs `print()` / `None` | Aug 30 | done | done (Sep 1 context) | pending (Sep 6) | pending |
| f-strings + `TypeError` (str+int) | Aug 30 | done | pending (Sep 2) | pending (Sep 6) | pending |
| Lists - indexing/append/insert/remove/pop/sort/slice/copy | Aug 31 | done (Sep 1) | pending (Sep 3) | pending (Sep 7) | pending |

## Next session priorities (in order)

1. **Chapter 4 (this session)** - teach properly from scratch: for-loop over list items, range() + numerical lists, simple statistics (min/max/sum), list comprehensions, tuples. Same LEARN -> SEE -> CODE -> PRACTICE cycle as Ch 2 and Ch 3.
2. **HackerRank catch-up** - submit Print Function and Lists once Chapter 4 for-loop practice is solid (3/5 done, 2 remain, Week 1 target was ~8 so still behind).
3. **LeetCode access** - resolve network block (mobile data / different network), then attempt #217, #26, #1.
4. Remember: ask for a written prediction *before* running code on at least one exercise per session.

## Legend

Not started -> Attempted/In progress -> Solved (with help) -> Solved independently -> Needs revision
