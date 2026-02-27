"""
LeetCode 217 - Contains Duplicates
Pattern: Hashing

Approach 1: Brute Force (Sort and traverse checking adjacent pairs)
Time: O(nlogn)
Space: O(1)

Approach 2: Better and Optimal (HashMap)
Time: O(n)
Space: O(n)

"""
from typing import List


# ---------------- BRUTE FORCE ----------------
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False

# ---------------- OPTIMAL SOLUTION ----------------
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
  
        seen={}
        for i,num in enumerate(nums):
            if num in seen:
                return True
            seen[num]=i
        return False