"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy

Given an array of integers nums and an integer target, return the indices of 
the two numbers that add up to target.

You may assume that each input has exactly one solution, and you may not use 
the same element twice.

Example:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: nums[0] + nums[1] == 9, so we return [0, 1].

Approach: Hash Map
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers that add up to target using hash map.

        Algorithm:
        1. Create a hash map to store number -> index mapping
        2. Iterate through array
        3. For each number, check if (target - number) exists in hash map
        4. If yes, return the indices
        5. If no, add current number to hash map and continue

        Args:
            nums: List of integers
            target: Target sum

        Returns:
            List containing indices of two numbers
        """
        # Dictionary to store number -> index mapping
        seen = {}

        for i, num in enumerate(nums):
            # Calculate complement needed to reach target
            complement = target - num

            # Check if complement exists in our hash map
            if complement in seen:
                # Return indices (seen has the first index, i is current)
                return [seen[complement], i]

            # Store current number with its index
            seen[num] = i

        # Should never reach here as problem guarantees a solution
        return []


# ============================================================================
# APPROACH COMPARISON
# ============================================================================

class Solution_BruteForce:
    """
    Brute Force Approach: Nested Loop
    Time Complexity: O(n²)
    Space Complexity: O(1)

    Not Optimal: Checks every pair, inefficient for large arrays
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Check all pairs
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# ============================================================================
# COMPLEXITY ANALYSIS
# ============================================================================
"""
OPTIMAL SOLUTION (Hash Map):
├── Time Complexity: O(n)
│   └── Single pass through array
│   └── Hash map operations (insert, lookup) are O(1) average
│
└── Space Complexity: O(n)
    └── Hash map stores up to n elements

BRUTE FORCE (Nested Loop):
├── Time Complexity: O(n²)
│   └── Nested loops check all pairs
│   └── Total operations: n * (n-1) / 2
│
└── Space Complexity: O(1)
    └── Only uses constant extra space
"""


# ============================================================================
# TEST CASES
# ============================================================================

def test_two_sum():
    """Test cases for two sum problem"""
    solution = Solution()

    # Test case 1: Basic example
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    print("PASS: Test 1 passed: [2,7,11,15], target=9")

    # Test case 2: Different order
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    print("PASS: Test 2 passed: [3,2,4], target=6")

    # Test case 3: Duplicates
    result = solution.twoSum([3, 3], 6)
    assert result == [0, 1]
    print("PASS: Test 3 passed: [3,3], target=6")

    # Test case 4: Larger array
    assert solution.twoSum([2, 5, 5, 11], 10) == [1, 2]
    print("PASS: Test 4 passed: [2,5,5,11], target=10")

    print("\nAll tests passed!")


if __name__ == "__main__":
    # Run tests
    test_two_sum()

    # Example usage
    print("\n" + "="*50)
    print("Example Usage:")
    print("="*50)

    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")
    print(f"Explanation: nums[{result[0]}] + nums[{result[1]}] = {target}")
