"""
LeetCode 560 - Subarray Sum equals K
Pattern: Prefix Sum

Approach 1: Brute Force (Generate all subarrays)
Time: O(n3)
Space: O(1)

Approach 2: Better and Optimal (HashMap)
Time: O(n)
Space: O(n)

"""
# ---------------- BRUTE FORCE ----------------
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            for j in range(i, n):
                total = 0
                for p in range(i, j + 1):
                    total += nums[p]
                if total == k:
                    count += 1

        return count
# ---------------- BETTER SOLUTION ----------------

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                if total == k:
                    count += 1

        return count
# ---------------- OPTIMAL SOLUTION ----------------

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        presum=0
        prefixsum={0:1}
        for num in nums:
            presum+=num
            diff = presum-k
            res+=prefixsum.get(diff,0)

            prefixsum[presum]=1+prefixsum.get(presum,0)
        return res
        