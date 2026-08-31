# Progress Dashboard

*Last updated: Aug 31, 2026 (Day 2)*

```
Python Core (Ch. 1-11):     3 / 11 chapters        [######              ] ~27%
Book Try-It-Yourself done:  0 / 68  (working via live custom exercises instead)
HackerRank solved:           0
DSA topics covered:          0 / 15               [                    ] 0%
LeetCode solved:              0 / 200              [                    ] 0%
  Easy:   0 / 80
  Medium: 0 / 102
  Hard:   0 / 18
Current week:                Week 1 (Aug 30 - Sep 5)
Current day:                 Day 2
Current streak:               2 days
Weekly test average:          - (Test #1 due end of Week 1)
Days elapsed / total:         1.5 / 94
Schedule status:              AHEAD OF PACE. Ch1-3 done. HackerRank still at 0 - must start next session.
```

## Concepts confirmed solid (through live exercises, not just reading)

| Concept | Status | Evidence |
|---|---|---|
| `print()`, variables, `=` as storage not equality | Solid | Baseline Q3 misunderstood -> corrected same day |
| f-strings | Solid | Multiple correct independent uses |
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

## Revision Queue (spaced repetition)

| Concept | Date Learned | Review @ 1d | Review @ 3d | Review @ 7d | Review @ 14d |
|---|---|---|---|---|---|
| `return` vs `print()` / `None` | Aug 30 | done (used again Aug 31 context) | pending (Sep 2) | pending (Sep 6) | pending |
| f-strings + `TypeError` (str+int) | Aug 30 | done | pending (Sep 2) | pending (Sep 6) | pending |
| Lists - indexing/append/insert/remove/pop/sort/slice/copy | Aug 31 | pending (Sep 1) | pending (Sep 3) | pending (Sep 7) | pending |

## Next session priorities (in order)

1. **HackerRank catch-up** - still 0 solved, Week 1 target was ~8. Start with 3 problems matched to variables/strings/lists (no advanced topics needed yet).
2. Move into Chapter 4 (`for` loops, `while` loops) using the same LEARN -> SEE -> CODE -> PRACTICE cycle.
3. Remember: ask for a written prediction *before* running code on at least one exercise per session (skipped once on Aug 31, no harm done but should become a habit).

## Legend

Not started -> Attempted/In progress -> Solved (with help) -> Solved independently -> Needs revision
