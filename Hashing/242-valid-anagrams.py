"""
LeetCode 242 - Valid Anagrams
Pattern: Hashing

Approach 1: Brute Force (Sorted check)
Time: O(nlogn)
Space: O(1)

Approach 2: Better and Optimal(HashMap- store char counts)
Time: O(n)
Space: O(n)


"""
# ---------------- BRUTE FORCE ----------------
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        return sorted(s)==sorted(t)
       
# ---------------- OPTIMAL SOLUTION ----------------

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
      
        count={}
        for ch in s:
            count[ch]=1+count.get(ch,0)
        for ch in t:
            
            if ch not in count:
                return False
            count[ch] -=1
            if count[ch]==0:
                del count[ch]
        return len(count)==0
