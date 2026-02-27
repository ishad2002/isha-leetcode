"""
LeetCode 238 - Product Except Self
Pattern: Prefix Sum

Approach 1: Brute Force (Generate all products)
Time: O(n2)
Space: O(1)

Approach 2: Better and Optimal (HashMap)
Time: O(n)
Space: O(n)

"""
from typing import List
# ---------------- BRUTE FORCE ----------------
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        for i in range(n):
            product = 1
            for j in range(n):
                if i != j:
                    product *= nums[j]
            res.append(product)

        return res
    
# ---------------- BETTER SOLUTION ----------------
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total_product *= num

        res = []

        for num in nums:
            if zero_count > 1:
                res.append(0)
            elif zero_count == 1:
                if num == 0:
                    res.append(total_product)
                else:
                    res.append(0)
            else:
                res.append(total_product // num)

        return res
    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[1]*n
        prefix=[1]*n
        suffix=[1]*n
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]*nums[i-1]
        # for i in range(1,len(nums)):
        #     ans[i]=ans[i-1]*nums[i-1]
        # suffix=1
        # for i in range(len(nums)-2,-1,-1):
        #     suffix=suffix*nums[i+1]
        #     ans[i]=ans[i]*suffix
        for i in range(len(nums)-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i+1]
        for i in range(len(nums)):
            ans[i]=prefix[i]*suffix[i]
        return ans
# ---------------- OPTIMAL SOLUTION ----------------
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        # Prefix pass
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]

        # Suffix pass
        suffix = 1
        for i in range(n-2, -1, -1):
            suffix *= nums[i+1]
            ans[i] *= suffix

        return ans
    
