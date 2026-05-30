# Contributing to DSA 365

Thank you for your interest in contributing! Here's how you can help.

## Ways to Contribute

1. **Add new problem solutions**
2. **Improve existing solutions**
3. **Fix bugs or typos**
4. **Add explanations and comments**
5. **Create new cheat sheets**
6. **Improve documentation**

## Getting Started

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/add-problem-x`
3. Make your changes
4. Commit with clear messages: `git commit -m "dsa: add two-sum solution"`
5. Push to branch: `git push origin feature/add-problem-x`
6. Submit a Pull Request

## Problem Solution Guidelines

### File Naming
```
problems/[topic]/[problem-number]-[problem-name].py
Example: problems/01-arrays/001-two-sum.py
```

### Solution Template
```python
"""
Problem: [Problem Name]
Link: [LeetCode/GeeksforGeeks Link]
Difficulty: Easy/Medium/Hard

Approach: [Algorithm Name]
Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution:
    def method_name(self, params):
        """
        Detailed explanation.
        """
        pass

# Test cases
def test():
    sol = Solution()
    # Test 1
    assert sol.method_name(input1) == expected1
    # Test 2
    assert sol.method_name(input2) == expected2
```

## Commit Message Format

```
<type>: <subject>

<body>

<footer>
```

### Types
- `dsa`: DSA problem solution
- `cheat`: Cheat sheet updates
- `docs`: Documentation
- `fix`: Bug fixes
- `feat`: New features

### Example
```
dsa: add two-sum solution with hash map

Implemented optimal O(n) solution using hash map.
Includes brute force comparison and test cases.

Closes #1
```

## Code Quality

- Clear variable names
- Proper indentation (4 spaces)
- Comments for complex logic
- Type hints where applicable
- Comprehensive docstrings

## Questions?

Open an issue or reach out via email: chandusri203@gmail.com

Thank you for contributing! 🙏