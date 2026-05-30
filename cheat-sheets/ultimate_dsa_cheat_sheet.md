# Ultimate DSA Cheat Sheet 📚

> Complete reference guide for Data Structures & Algorithms

---

## Table of Contents
1. [Big O Complexity](#big-o-complexity)
2. [Arrays](#arrays)
3. [Strings](#strings)
4. [Linked Lists](#linked-lists)
5. [Stacks & Queues](#stacks--queues)
6. [Trees](#trees)
7. [Graphs](#graphs)
8. [Sorting](#sorting)
9. [Dynamic Programming](#dynamic-programming)
10. [Binary Search](#binary-search)

---

## Big O Complexity

### Time Complexity Chart

```
O(1)      Constant Time      - Best
O(log n)  Logarithmic
O(n)      Linear
O(n log n) Linearithmic
O(n²)     Quadratic
O(n³)     Cubic
O(2ⁿ)     Exponential
O(n!)     Factorial         - Worst
```

### Common Operations

| Operation | Time Complexity |
|-----------|------------------|
| Array Access | O(1) |
| Array Search | O(n) |
| Array Insertion | O(n) |
| Array Deletion | O(n) |
| Hash Lookup | O(1) avg, O(n) worst |
| Tree Search | O(log n) to O(n) |
| Graph Search | O(V + E) |

---

## Arrays

### Key Points
- Fixed size (in most languages)
- Random access: O(1)
- Linear search: O(n)
- Insertion/Deletion: O(n)

### Common Patterns

**Two Pointers**
```python
left, right = 0, len(arr) - 1
while left < right:
    # Do something
    left += 1
    right -= 1
```

**Sliding Window**
```python
left = 0
for right in range(len(arr)):
    # Expand window
    while condition:
        # Shrink window
        left += 1
```

**Prefix Sum**
```python
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i+1] = prefix[i] + arr[i]
```

### Common Problems
- Two Sum
- Container With Most Water
- Best Time to Buy Stock
- Maximum Subarray
- Product of Array Except Self

---

## Strings

### Key Points
- Similar to arrays in many languages
- Immutable in Python/Java
- Common operations: substring, reverse, split

### String Manipulation Patterns

**Palindrome Check**
```python
s == s[::-1]  # Python
```

**Character Frequency**
```python
from collections import Counter
freq = Counter(s)
```

**Anagram Check**
```python
Counter(s1) == Counter(s2)
```

### Common Problems
- Valid Parentheses
- Longest Substring Without Repeating
- Group Anagrams
- Longest Palindromic Substring
- Regular Expression Matching

---

## Linked Lists

### Node Structure
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### Key Operations
- Traverse: O(n)
- Search: O(n)
- Insertion: O(1) - if node position known
- Deletion: O(1) - if node position known

### Common Patterns

**Fast & Slow Pointers**
```python
slow, fast = head, head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

**Reverse Linked List**
```python
prev, curr = None, head
while curr:
    next_temp = curr.next
    curr.next = prev
    prev = curr
    curr = next_temp
return prev
```

### Common Problems
- Reverse Linked List
- Merge Two Sorted Lists
- Linked List Cycle
- LRU Cache
- Reorder List

---

## Stacks & Queues

### Stack (LIFO)
```python
from collections import deque
stack = deque()
stack.append(x)      # Push
val = stack.pop()    # Pop
top = stack[-1]      # Peek
```

### Queue (FIFO)
```python
from collections import deque
queue = deque()
queue.append(x)      # Enqueue
val = queue.popleft()  # Dequeue
front = queue[0]     # Peek
```

### Common Problems
- Valid Parentheses
- Daily Temperatures
- Largest Rectangle in Histogram
- Implement Queue using Stacks
- Min Stack

---

## Trees

### Node Structure
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### Tree Traversals

**Inorder (Left-Root-Right)**
```python
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```

**Preorder (Root-Left-Right)**
```python
def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)
```

**Postorder (Left-Right-Root)**
```python
def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]
```

**Level Order (BFS)**
```python
from collections import deque
def levelOrder(root):
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
```

### Binary Search Tree (BST)
- Left < Root < Right
- Search: O(log n) avg, O(n) worst
- Insert: O(log n) avg
- Delete: O(log n) avg

### Common Problems
- Binary Tree Level Order Traversal
- Lowest Common Ancestor
- Validate Binary Search Tree
- Kth Smallest Element in BST
- Serialize and Deserialize Binary Tree

---

## Graphs

### Graph Representation

**Adjacency List**
```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}
```

**Adjacency Matrix**
```python
graph = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0]
]
```

### DFS (Depth-First Search)
```python
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited
```

### BFS (Breadth-First Search)
```python
from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited
```

### Dijkstra's Algorithm
```python
import heapq
def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist
```

### Common Problems
- Number of Islands
- Course Schedule
- Graph Valid Tree
- Word Ladder
- Clone Graph

---

## Sorting

### Comparison

| Algorithm | Time | Space | Stable |
|-----------|------|-------|--------|
| Bubble Sort | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(1) | No |
| Insertion Sort | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) avg | O(log n) | No |
| Heap Sort | O(n log n) | O(1) | No |
| Counting Sort | O(n+k) | O(k) | Yes |

### Quick Sort
```python
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1
```

### Merge Sort
```python
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

---

## Dynamic Programming

### Key Concept
1. **Optimal Substructure** - Problem can be broken into overlapping subproblems
2. **Memoization** - Store results of subproblems to avoid recomputation
3. **Tabulation** - Build solutions bottom-up

### Pattern Recognition

**Linear DP**
- Fibonacci, House Robber, Climbing Stairs

**2D DP**
- Longest Common Subsequence, Edit Distance

**Knapsack**
- 0/1 Knapsack, Unbounded Knapsack

### Example: Climbing Stairs
```python
# Recursive with Memoization
def climbStairs(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return n
    memo[n] = climbStairs(n-1, memo) + climbStairs(n-2, memo)
    return memo[n]

# Tabulation
def climbStairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

### Common Problems
- Fibonacci
- House Robber
- Coin Change
- Longest Increasing Subsequence
- Edit Distance

---

## Binary Search

### Template
```python
def binarySearch(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### Key Points
- Only works on sorted arrays
- Time Complexity: O(log n)
- Space Complexity: O(1) or O(log n) for recursion

### Common Problems
- Binary Search
- Search in Rotated Sorted Array
- Find First and Last Position
- Median of Two Sorted Arrays
- Kth Smallest Element

---

## Problem-Solving Tips

✅ **Understand the Problem**
- Read carefully
- Identify input/output
- Consider edge cases

✅ **Plan Your Approach**
- Think about brute force first
- Optimize step by step
- Consider different data structures

✅ **Code Your Solution**
- Start with pseudocode
- Write clear variable names
- Add comments

✅ **Test Your Solution**
- Test with provided examples
- Test edge cases
- Test with large inputs

✅ **Optimize**
- Check time complexity
- Reduce space complexity
- Refactor for readability

---

**Master these concepts, and you're ready for any DSA interview! 🚀**