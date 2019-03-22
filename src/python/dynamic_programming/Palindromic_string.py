"""
#647 palindromic string

https://leetcode.com/problems/palindromic-substrings/

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
        n = len(s)
        result = [[0] * n for _ in range(n)]
        # each char in s is a palindromic string
        for i in range(n):
            result[i][i] = 1
        
        for i in range(n - 2, -1, -1):
            for j in range(n):
                if j - i > 2:
                    result[i][j] = 1 if s[i] == s[j] and result[i+1][j-1] else 0
                else:
                    result[i][j] = 1 if s[i] == s[j] else 0
        return sum(sum(l) for l in result)


if __name__ == "__main__":
    s = 'abc'
    print(Solution().countSubstrings(s))
