"""
LeetCode 53 - Maximum Subarray
Pattern: Prefix Sum

Approach 1: Better and Optimal (Kadane)
Time: O(n)
Space: O(1)

"""
import math
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        maxsum=-math.inf
        # if len(nums)==0:
        #     return -1
        for num in nums:
            sum+=num
            
            maxsum = max(sum,maxsum)

            if sum<0:
                sum=0
        return maxsum

        