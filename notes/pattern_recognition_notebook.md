# Pattern Recognition Notebook

Filled in as each pattern is covered. Goal: scan "Trigger Clues" before writing a line of code.

| Pattern | Trigger Clues | Core Idea | Template Skeleton | Problems Solved |
|---|---|---|---|---|
| Two Pointers | "sorted array", "pair that sums to", palindrome check | Move two indices toward/away from each other | `l, r = 0, len(arr)-1` while `l < r` | |
| Sliding Window | "substring/subarray of length k", "longest/shortest..." | Maintain a window, expand/shrink | `l = 0; for r in range(n): ... while invalid: l += 1` | |
| Prefix Sum | "sum of subarray", "range sum queries" | Precompute cumulative sums | `prefix[i] = prefix[i-1] + arr[i]` | |
| Hashing / Frequency Map | "count occurrences", "duplicate", "anagram" | Trade space for O(1) lookup | `dict()` or `Counter()` | |
| Fast & Slow Pointers | "linked list", "cycle", "middle of list" | Two pointers at different speeds | `slow, fast = head, head` | |
| Binary Search | "sorted array", "minimize/maximize X such that..." | Halve search space | `lo, hi = 0, n-1; while lo <= hi:` | |
| Monotonic Stack | "next greater/smaller element" | Maintain increasing/decreasing stack | `stack = []` push/pop while condition | |
| BFS | "shortest path unweighted", "level order" | Explore level by level | `deque`, visited set | |
| DFS | "all paths", "connected components" | Go deep first, backtrack | recursion or explicit stack | |
| Backtracking | "all subsets/permutations/combinations" | Try, recurse, undo | `def bt(path, choices): ... bt(...); path.pop()` | |
| Heap / Top-K | "k largest/smallest", "merge k sorted" | Maintain a heap of size k | `heapq` | |
| Greedy | "maximize/minimize", "intervals", "scheduling" | Locally optimal choice | sort + single pass usually | |
| Dynamic Programming | "count ways", "min/max cost", "optimal subsequence" | Overlapping subproblems, cache | define state -> transition -> base case | |
