"""
#91 decode ways

https://leetcode.com/problems/decode-ways/


A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        result = [1] + [0 for _ in range(len(s))]
        for i in range(1, len(s) + 1):
            pre1 = result[i-1] if i - 1 >= 0 and int(s[i-1]) >= 1 else 0
            pre2 = (result[i-2] if i - 2 >= 0 and 1 <= int(s[i-2:i]) <= 26 else 0)
            result = pre1 + pre2
        return result[-1]


if __name__ == "__main__":
    s = "12"
    s2 = "226"
    print(Solution().numDecodings(s))
    print(Solution().numDecodings(s2))
