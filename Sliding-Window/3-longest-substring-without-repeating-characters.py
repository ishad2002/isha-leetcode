"""
LeetCode 3 - Longest Substring Without Repeating Characters
Pattern: Sliding Window

Approach 1: Brute Force (Generate All Substrings)
Time: O(n^3)
Space: O(1)

Approach 2: Better (HashMap)
Time: O(n^2)
Space: O(256)

Approach 3: Optimal (Sliding Window + Set)
Time: O(n)
Space: O(256)
"""


# ---------------- BRUTE FORCE ----------------
class SolutionBrute:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
        
        for i in range(n):
            for j in range(i,n):
                substring=s[i:j+1]
                if len(set(substring)) == len(substring):
                    max_len=max(max_len,j-i+1)
        return max_len
    
# set(substring) - builds a set from k characters (k=n worst case)

# ---------------- BETTER SOLUTION ----------------

class SolutionBetter:
    def lengthOfLongestSubstring(self,s: str) -> int:
        max_len=0
        n=len(s)
        for i in range (n):
            charHash=[0]*256

            for j in range(i,n):

                if charHash[ord(s[j])]==1:
                    break
                currlen=j-i+1
                max_len=max(currlen,max_len)
                charHash[ord(s[j])]=1
        return max_len

# ---------------- OPTIMAL SOLUTION ----------------

class Solution:
    def lengthOfLongestSubstring(self,s:str)->int:
        charHash=[-1]*256
        l=r=max_len=0
        n=len(s)
        while r<n:
            if charHash[ord(s[r])]!=-1:
                if charHash[ord(s[r])]>=l:
                    l=charHash[ord(s[r])]+1
            currlen=r-l+1
            max_len=max(currlen,max_len)

            charHash[ord(s[r])]=r
            r=r+1
        return max_len


