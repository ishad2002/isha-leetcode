"""
LeetCode 1004 - Max Consecutive Ones III
Pattern: Sliding Window

------------------------------------------------------
Approach 1: Brute Force
------------------------------------------------------
Idea:
Generate all subarrays and check if we can make the entire
subarray all 1s by flipping at most k zeros.

For every subarray:
zeros_count <= k → valid subarray

Time Complexity: O(n^2)
Space Complexity: O(1)

------------------------------------------------------
Approach 2: Optimal Sliding Window
------------------------------------------------------
Idea:
Maintain a window with at most k zeros.

Expand window when zeros_count <= k.
Shrink from left when zeros_count > k.

This ensures we always track the longest valid window.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:

    # -------------------------------------------------
    # Approach 1: Brute Force
    # -------------------------------------------------
    def longestOnes_bruteforce(self, nums, k: int) -> int:
        n = len(nums)
        max_len = 0

        for i in range(n):
            zeros = 0
            for j in range(i, n):
                if nums[j] == 0:
                    zeros += 1

                if zeros <= k:
                    max_len = max(max_len, j - i + 1)
                else:
                    break   # further expansion only increases zeros

        return max_len


    # -------------------------------------------------
    # Approach 2: Optimal Sliding Window
    # -------------------------------------------------
    def longestOnes(self, nums, k: int) -> int:
        l = 0
        zero_count = 0
        max_len = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zero_count += 1

            # shrink window if invalid
            while zero_count > k:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len
