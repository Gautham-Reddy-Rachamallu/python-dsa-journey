# Progress Dashboard

*Last updated: Sep 5, 2026 (Day 7)*

```
Python Core (Ch. 1-11):     4 / 11 chapters        [########            ] ~36%
Book Try-It-Yourself done:  0 / 68  (working via live custom exercises instead)
HackerRank solved:           3 / 5 (Week 1 target ~8) - 2 unblocked, ready to submit
DSA topics covered:          0 / 15               [                    ] 0%
LeetCode solved:              0 / 200              [                    ] 0%
  Easy:   0 / 80
  Medium: 0 / 102
  Hard:   0 / 18
Current week:                Week 1 (Aug 30 - Sep 5)
Current day:                 Day 7 (end of Week 1)
Current streak:               4 sessions
Weekly test average:          - (Test #1 due end of Week 1)
Days elapsed / total:         6 / 94
Schedule status:              Chapters ahead of pace (Ch 1-4 done vs Week-1 target of Ch 1-2). HackerRank behind (3/8). LeetCode at 0, still blocked by network issue - needs resolving this week.
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
| `for item in list:` direct iteration + filtering pattern | Solid | Correct first try on fruits/nums>4/evens; independently distinguished loop-variable vs list-variable behavior unprompted |
| `range(start, stop)` + numerical lists + `min()/max()/sum()` | Solid | All 4 exercises correct first try, including the exact Print Function HackerRank output (`123456789`) |
| List comprehensions `[expr for x in iterable if cond]` | Solid (after 1 correction) | 3/4 correct first try; 1 real bug caught (typo `even` vs `evens` masked by stale notebook variable) - understood and fixed correctly |
| Tuples - immutability, indexing/looping like lists, `TypeError` on item assignment | Solid | All 4 exercises correct; explained the TypeError in own words correctly; also self-corrected `range(len())` style to direct iteration when flagged |

## HackerRank Log (Week 1)

| Problem | Status | Notes |
|---|---|---|
| Say "Hello, World!" | Accepted | Score 5.00 |
| Arithmetic Operators | Accepted | 10 pts, all test cases passed |
| Python: Division | Accepted | 10 pts, correctly handled int/int -> float vs // |
| Print Function | Unblocked, not yet submitted | Chapter 4 range()/end="" practice produced exact correct output (`123456789`) - ready to submit on the actual platform |
| Lists | Unblocked, not yet submitted | Chapter 4 for-loop practice complete - ready to build the if/elif command chain and submit |

## LeetCode Log

| # | Problem | Status | Notes |
|---|---|---|---|
| 217 | Contains Duplicate | Blocked | LeetCode.com not loading - suspected network/ISP block. Try mobile data or different network. |
| 26 | Remove Duplicates from Sorted Array | Blocked | Same as above |
| 1 | Two Sum | Blocked | Same as above |

## Weekly Test Score Log

| Week | Test Topic | Python (20%) | Coding (20%) | Problem Solving (20%) | DSA (20%) | LeetCode (10%) | Debugging (10%) | Total /100 |
|---|---|---|---|---|---|---|---|---|
| 1 | Ch 1-4 | | | | | | | pending - due end of Week 1 |

## Weak Topics / Error Log

| Date | Topic/Concept | What went wrong | Status |
|---|---|---|---|
| Aug 30 | `==` vs `=` | Thought `==` was assignment | Resolved same day |
| Aug 30 | `return` vs `print()` | Wrote `is_even` using `print()` inside `if`, got `None` in output | Resolved same day - rewrote with `return`, confirmed True/False |
| Aug 30 | Variable naming discipline | Swapped `first_name`/`last_name` values twice | Cosmetic, watch for it |
| Aug 31 | `.pop()` vs `.pop(0)` | Used `.pop()` (removes last) when asked to remove the first item | Resolved same session - corrected to `.pop(0)`, O(1) vs O(n) explained |
| Sep 1 | Curriculum sequencing | Two HackerRank problems (Print Function, Lists) assigned before loops were taught | Caught by Gautham, acknowledged - fixed by doing proper Chapter 4 before resuming those problems |
| Sep 2 | List comprehension typo (`even` vs `evens`) | Printed a different variable than the one just defined; didn't crash because a stale `evens` lingered from an earlier notebook cell, so it silently returned old/wrong data | Resolved same session - understood the notebook-state trap and rewrote correctly |
| Sep 2 | `range(len(list))` vs direct iteration | Used index-based looping (`for i in range(0,len(rgb)): print(rgb[i])`) where direct iteration was simpler and sufficient | Flagged, understood - reserve `range(len())` for cases needing the actual index |

## Revision Queue (spaced repetition)

| Concept | Date Learned | Review @ 1d | Review @ 3d | Review @ 7d | Review @ 14d |
|---|---|---|---|---|---|
| `return` vs `print()` / `None` | Aug 30 | done | done | done (Sep 6 due) | pending |
| f-strings + `TypeError` (str+int) | Aug 30 | done | done | done (Sep 6 due) | pending |
| Lists - indexing/append/insert/remove/pop/sort/slice/copy | Aug 31 | done | done | pending (Sep 7) | pending |
| for loops / range / comprehensions / tuples | Sep 1-2 | pending (Sep 3) | pending (Sep 5) | pending (Sep 9) | pending |

## Next session priorities (in order)

1. **Submit both unblocked HackerRank problems** - "Print Function" and "Lists" - on the actual HackerRank platform (both are code-ready from this session's practice).
2. **Resolve LeetCode network block** - try mobile data or a different network before next session; #217, #26, #1 are waiting.
3. **Move to Chapter 5 (if Statements)** - conditionals, boolean logic, `in`/`not in` - using the same LEARN -> SEE -> CODE -> PRACTICE cycle. Note: basic `if` has already been used informally (is_even, filtering loops), so this chapter can move a bit faster while still covering `in`/`not in` and full boolean logic properly.
4. Continue the habit of a written prediction before running code on at least one exercise per session.

## Legend

Not started -> Attempted/In progress -> Solved (with help) -> Solved independently -> Needs revision
