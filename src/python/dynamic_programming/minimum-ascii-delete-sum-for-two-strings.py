"""
Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
Example 2:
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
Note:

0 < s1.length, s2.length <= 1000.
All elements of each string will have an ASCII value in [97, 122].

Source: https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/
"""

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        l1, l2 = len(s1), len(s2)
        # dp_sums[i][j] means the minimum delete sum for string s1[i:] and s2[j:]
        dp_sums = [[0] * (l2 + 1) for _ in range(l1 + 1)]

        for i in range(l1 - 1, -1, -1):
            dp_sums[i][l2] = dp_sums[i+1][l2] + ord(s1[i])
            
        for i in range(l2 - 1, -1, -1):
            dp_sums[l1][i] = dp_sums[l1][i+1] + ord(s2[i])

        for i in range(l1 - 1, -1, -1):
            for j in range(l2 - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp_sums[i][j] = dp_sums[i+1][j+1]
                else:
                    dp_sums[i][j] = min(dp_sums[i+1][j] + ord(s1[i]), dp_sums[i][j+1] + ord(s2[j]))

        return dp_sums[0][0]

if __name__ == "__main__":
    s1 = "sea"
    s2 = "eat"
    s12 = "delete"
    s22 = "leet"
    print(Solution().minimumDeleteSum(s1, s2))
    print(Solution().minimumDeleteSum(s12, s22))
