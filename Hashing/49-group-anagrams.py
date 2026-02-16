"""
LeetCode 49 - Group Anagrams
Pattern: Hashing

Approach 1: Brute Force (key - sorted word)
Time: O(nlogn)
Space: O(1)

Approach 2: Better and Optimal(key - char count array(indices count))
Time: O(n)
Space: O(256)

"""

from collections import defaultdict
from typing import List
# ---------------- BRUTE FORCE ----------------
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))   # signature by sorting
            groups[key].append(word)

        return list(groups.values())


    
# ---------------- OPTIMAL SOLUTION ----------------

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)

        for word in strs:
            count = [0] * 26   # for a–z

            for ch in word:
                count[ord(ch) - ord('a')] += 1

            key = tuple(count)   # tuple can be dict key
            groups[key].append(word)

        return list(groups.values())