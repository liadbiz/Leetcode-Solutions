"""
#139 word break

https://leetcode.com/problems/word-break/

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""
from typing import List

class Solution:
    # time limit exceeded
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def canBreak(s):
            if s in wordDict:
                return True
            for w in wordDict:
                if s[-(len(w)):] == w:
                    return canBreak(s[:-(len(w))])
            return False
        return canBreak(s)                    

    # zccept
    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        min_len = float('inf')
        for w in wordDict:
            min_len = min(min_len, len(w))
        if n < min_len:
            return False
        result = [True] + [False] * n
        for i in range(min_len, n+1):
            for w in wordDict:
                if result[i-len(w)] == True and w == s[i-len(w):i]:
                    result[i]= True
        return result[-1]


if __name__ == "__main__":
    s, wordDict = "leetcode", ["leet", "code"]
    s2, wordDict2 = "applepenapple", ["apple", "pen"]
    s3, wordDict3 = "catsandog", ["cats", "dog", "sand", "and", "cat"]
    # test method 1
    print(Solution().wordBreak(s, wordDict))
    print(Solution().wordBreak(s2, wordDict2))
    print(Solution().wordBreak(s3, wordDict3))
    # test method 2
    print(Solution().wordBreak2(s, wordDict))
    print(Solution().wordBreak2(s2, wordDict2))
    print(Solution().wordBreak2(s3, wordDict3))
