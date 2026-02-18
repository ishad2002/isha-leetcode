"""
LeetCode 424 - Longest Repeating Character Replacement
Pattern: Sliding Window

------------------------------------------------------
Approach 1: Brute Force
------------------------------------------------------
Idea:
Generate all substrings and check if they can be made
of one repeating character using at most k replacements.

For every substring:
replacements_needed = window_size - max_frequency_char

If replacements_needed <= k → valid substring.

Time Complexity: O(n^3)
Space Complexity: O(26) ~ O(1)

------------------------------------------------------
Approach 2: Optimal Sliding Window
------------------------------------------------------
Idea:
Maintain a window where:
(window_size - max_frequency_char) <= k

Expand window if valid.
Shrink from left if invalid.

Important Trick:
We do NOT decrease max_frequency when shrinking.
Even if it becomes slightly outdated, result remains correct
and keeps algorithm O(n).

Time Complexity: O(n)
Space Complexity: O(26) ~ O(1)
"""


class Solution:

    # -------------------------------------------------
    # Approach 1: Brute Force
    # -------------------------------------------------
    def characterReplacement_bruteforce(self, s: str, k: int) -> int:
        n = len(s)
        max_len = 0

        for i in range(n):
            for j in range(i, n):
                freq = [0] * 26
                maxf = 0

                # count frequency in substring s[i..j]
                for t in range(i, j + 1):
                    idx = ord(s[t]) - ord('A')
                    freq[idx] += 1
                    maxf = max(maxf, freq[idx])

                # replacements needed
                changes = (j - i + 1) - maxf

                if changes <= k:
                    max_len = max(max_len, j - i + 1)

        return max_len


    # -------------------------------------------------
    # Approach 2: Optimal Sliding Window
    # -------------------------------------------------
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # hash = [-1]*256
        # l=0
        # r=0
        # maxlen=0
        # maxf=0
        # for i in range(len(s)):
        #     hash=[0]*26
        #     for j in range(i,len(s)):
        #         hash[ord(s[j]) - ord('A')]=1+hash[ord(s[j]) - ord('A')]
        #         maxf=max(maxf,hash[ord(s[j]) - ord('A')])
        #         changes=(j-i+1)-maxf

        #         if changes<=k:
        #             maxlen=max(maxlen,j-i+1)
        #         else:
        #             break
        # return maxlen
       
        l=0
        j=0
        maxlen=0
        maxf=0
        hash=[0]*26
        while j<len(s):
            hash[ord(s[j]) - ord('A')]+=1
            maxf=max(maxf,hash[ord(s[j]) - ord('A')])

            if (j-l+1)-maxf >k:
                hash[ord(s[l]) - ord('A')]-=1
                l=l+1
           
            maxlen=max(maxlen,j-l+1)
            j=j+1
        return maxlen




        