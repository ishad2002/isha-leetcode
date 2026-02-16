"""
LeetCode 1 - Two Sum
Pattern: Hashing

Approach 1: Brute Force (Generate All pairs and check sum==target)
Time: O(n^2)
Space: O(1)

Approach 2: Better and Optimal(HashMap - store indices)
Time: O(n)
Space: O(n)

"""

# ---------------- BRUTE FORCE ----------------

class Solution(object):
    def twoSumBrute(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target == nums[i]+nums[j]:
                    res.append(i)
                    res.append(j)
                    break
        return res

# ---------------- OPTIMAL SOLUTION ----------------
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
     
        seen={}
        for i in range(len(nums)):
            complement = target-nums[i]

            if complement in seen:
                return [i,seen[complement]]
            seen[nums[i]]=i

        