"""
LeetCode 34 - Find First and Last Position of Element in Sorted Array
Pattern: Binary Search

"""
from typing import List

class Solution:
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first(arr,target):
            low=0
            high=len(arr)-1
            ans=-1
            while low<=high:
                mid=(low+high)//2
                if arr[mid]==target:
                    ans=mid
                    high=mid-1
                elif arr[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return ans
        def last(arr,target):
            low=0
            high=len(arr)-1
            ans=-1
            while low<=high:
                mid=(low+high)//2
                if arr[mid]==target:
                    ans=mid
                    low=mid+1
                elif arr[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return ans
        return [first(nums,target),last(nums,target)]
        