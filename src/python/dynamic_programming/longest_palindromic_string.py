"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for i in range(1, len(s) - 1):
            start, end = i, i
            if s[i - 1] == s[i + 1]:
                start = i - 1
                end = i + 1
            elif s[i] == s[i + 1]:
                start = i - 1
                end = i + 2
            elif s[i] == s[i - 1]:
                start = i - 2
                end = i + 1 
            while start >=0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            res = s[start + 1:end] if (end - start) > len(res) else res
        if len(list(set(s))) <= 1:
            return s
        elif res == '':
            return s[0]
        else:
            return res

                
        


if __name__ == "__main__":
    s = 'babad'
    s2 = 'cbbd'
    s3 = ''
    s4 = 'a'
    s5 = 'ab'
    s6 = 'aa'
    print(Solution().longestPalindrome(s))
    print(Solution().longestPalindrome(s2))
    print(Solution().longestPalindrome(s3))
    print(Solution().longestPalindrome(s4))
    print(Solution().longestPalindrome(s5))
    print(Solution().longestPalindrome(s6))
