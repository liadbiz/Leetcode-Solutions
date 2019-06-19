"""
647. Palindromic Substrings
source: https://leetcode-cn.com/problems/palindromic-substrings/

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Note:

The input string length won't exceed 1000.

"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s: return 0
        res = len(s)
        dp = [[i,i+1] for i in range(len(s))]
        for i in range(1, len(s)):
            for j in dp[i-1]:
                if j-1 >= 0 and s[j-1] == s[i]:
                    res += 1
                    dp[i].append(j-1)
        return res


if __name__ == "__main__":
    s = "aaa"
    print(Solution().countSubstrings(s))
