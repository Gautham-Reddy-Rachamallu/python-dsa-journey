# Book Analysis: Python Crash Course, 3rd Edition (Eric Matthes)

## Structure confirmed from the uploaded PDF

**Part I — Basics (Ch. 1–11):** this is our entire Python-core curriculum.
**Part II — Projects (Ch. 12–20):** Alien Invasion game (Pygame), Data Visualization, Django web app.

## Decision: Part II is SKIPPED (with one exception)

Part II is excellent Python practice but is optimized for game dev / web dev, not DSA or
interview prep. Time spent there does not move you toward 200 LeetCode problems. We will:
- **Skip Ch. 12–14** (Pygame game) and **Ch. 18–20** (Django) entirely — not relevant to your goal.
- **Optionally cherry-pick Ch. 15** (Generating Data — random walks, dice rolls with `plotly`)
  *only if* you want one extra loops/lists project. Not required.
- If you ever want a portfolio project later (post-Dec), Part II is still there — nothing is deleted,
  just deferred.

## Chapter-by-chapter mapping (Part I)

| Ch. | Chapter Title | Core Concepts | Coding Practice | HackerRank Focus | LeetCode Connection | DSA Connection |
|----|----|----|----|----|----|----|
| 1 | Getting Started | Running Python, editor setup, `print()`, syntax basics | Hello-world variants, simple scripts | I/O basics | — | Environment only, no DSA yet |
| 2 | Variables & Simple Data Types | Variables, strings (methods, f-strings), numbers, comments | String formatting drills, mini calculators | String basics, arithmetic | Warm-up for string problems later | Foundation for string manipulation |
| 3 | Introducing Lists | List creation, indexing, slicing, `sort()`/`sorted()` | Build/index/slice lists | List indexing/slicing problems | Arrays (Easy) | **Arrays — traversal, indexing** |
| 4 | Working with Lists | `for` loops over lists, list comprehensions, tuples, `range()` | Looping drills, comprehension rewrites | List processing | Arrays (Easy–Med) | **Arrays — traversal, prefix sum setup** |
| 5 | if Statements | Conditionals, boolean logic, `in`/`not in` | Conditional logic problems | Conditional drills | Arrays/Strings (Easy) | Branching logic used everywhere |
| 6 | Dictionaries | Key-value pairs, nesting, looping (`.items()`, `.keys()`, `.values()`) | Frequency counters, nested dict problems | Dict-based problems | Hashing (Easy–Med) | **Hashing — frequency maps, lookups** |
| 7 | User Input & while Loops | `input()`, `while`, `break`/`continue`, flags | Interactive programs | Loop-control problems | — | Loop invariants (used in two pointers) |
| 8 | Functions | `def`, positional/keyword/default args, `return`, `*args`/`**kwargs`, importing | Function-decomposition exercises | Function-based problems | — | **Recursion is layered in here (supplement)** |
| 9 | Classes | Class definition, `__init__`, methods, inheritance, importing classes | Small OOP models | OOP problems | Design-style LeetCode later | Needed for LinkedList/Tree/Graph node classes |
| 10 | Files & Exceptions | Reading/writing files, `try`/`except`/`else`/`finally`, JSON | File-processing scripts, error handling | Exception-handling problems | Edge-case handling mindset | Robust code for edge cases |
| 11 | Testing Your Code | `unittest`, test cases, assertions | Writing tests for your own functions | — | Verifying solutions before submitting | Practice for "test edge cases" step in our 10-step problem method |

## Exercises confirmed in the book

Your PDF contains **68 "Try It Yourself" exercises** across Ch. 1–11 — we will not skip these;
they're the fastest way to cement each concept before moving to HackerRank/LeetCode.

## Critical topics MISSING from the book (we supplement — non-negotiable for your goal)

The book is a *general intro*, not a DSA/interview book. These gaps get dedicated supplement
sessions layered into the roadmap at the point where you have the prerequisites:

| Missing Topic | Why it matters | When we add it |
|---|---|---|
| **Recursion** | Not covered at all; required for trees, backtracking, DP, divide-and-conquer | Week 5 (right after Functions) |
| **Big-O / complexity analysis** | Not covered; required for every DSA discussion | Week 6 |
| **Sets** | Mentioned only in passing | Week 3 (with Dictionaries) |
| **`collections` module** (`Counter`, `defaultdict`, `deque`) | Massively speeds up hashing/queue problems | Week 6–9 |
| **`heapq` module** | Required for heap/priority-queue problems | Week 12 |
| **Iterators & generators** (`yield`) | Not covered; good-to-know, Pythonic code | Week 6 (light touch) |
| **List/dict/set comprehensions (advanced)** | Book only covers basic list comprehensions | Week 4 & 6 |
| **Two pointers / sliding window as *named techniques*** | Book teaches the mechanics but never names the pattern | Week 6–8 |
| **Type hints, PEP 8 style depth** | Book is casual about style | Ongoing, light |
| **Sorting algorithm internals** (merge/quick sort from scratch) | Book only uses built-in `sort()` | Week 13 |

## Verdict

The book is a solid, correctly-ordered foundation for Ch. 1–11 and we will follow its sequence.
The supplement list above is what turns "finished the book" into "can actually solve problems,"
which is your stated non-negotiable requirement.
