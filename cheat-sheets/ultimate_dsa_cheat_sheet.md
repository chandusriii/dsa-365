# Ultimate DSA Cheat Sheet

Complete quick-reference for common DSA interview patterns.

## Big-O Order
`O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n) < O(n!)`

## Arrays
- Access: `O(1)`
- Search: `O(n)`
- Insert/Delete (middle): `O(n)`

Common patterns:
- Two pointers
- Sliding window
- Prefix sum

## Strings
- Hash map for frequency/counting
- Two pointers for palindrome checks
- Sliding window for unique/repeating constraints

## Linked Lists
- Traverse/Search: `O(n)`
- Insert/Delete with known node: `O(1)`

Core patterns:
- Fast and slow pointers
- In-place reverse
- Dummy head for edge-case handling

## Stack and Queue
- Stack (LIFO): push/pop/peek in `O(1)`
- Queue (FIFO): enqueue/dequeue in `O(1)` with `deque`

Use cases:
- Parentheses validation
- Monotonic stack problems
- BFS queue traversal

## Trees
Traversals:
- Inorder: Left, Root, Right
- Preorder: Root, Left, Right
- Postorder: Left, Right, Root
- Level-order: BFS

BST rule:
- Left subtree < node < right subtree

## Graphs
Representations:
- Adjacency list (most common)
- Adjacency matrix

Traversals:
- DFS: `O(V + E)`
- BFS: `O(V + E)`

Shortest path:
- Dijkstra (non-negative weights)

## Sorting
- Merge sort: `O(n log n)`, stable, extra space `O(n)`
- Quick sort: average `O(n log n)`, worst `O(n^2)`
- Heap sort: `O(n log n)`, in-place

## Dynamic Programming
Checklist:
1. Define state.
2. Define transition.
3. Set base case.
4. Choose memoization or tabulation.
5. Optimize space if possible.

Common DP families:
- 1D DP (Climbing Stairs, House Robber)
- 2D DP (LCS, Edit Distance)
- Knapsack variants

## Binary Search Template
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

## Interview Routine (30 min)
1. Understand input/output and constraints.
2. Write brute force first.
3. Improve with pattern recognition.
4. Validate with edge cases.
5. State final time/space complexity.
