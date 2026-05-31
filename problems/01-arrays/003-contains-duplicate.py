"""
Problem: Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy

Given an integer array nums, return True if any value appears at least twice,
and return False if every element is distinct.

Approach: Hash Set
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


def test_contains_duplicate() -> None:
    solution = Solution()

    assert solution.containsDuplicate([1, 2, 3, 1]) is True
    assert solution.containsDuplicate([1, 2, 3, 4]) is False
    assert solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    assert solution.containsDuplicate([]) is False

    print("All tests passed!")


if __name__ == "__main__":
    test_contains_duplicate()
