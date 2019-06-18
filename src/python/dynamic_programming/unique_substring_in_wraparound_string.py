"""
#467 Unique Substring In WrapAround String
source: https://leetcode-cn.com/problems/unique-substrings-in-wraparound-string/

Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.

Example 1:
Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.
Example 2:
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.
Example 3:
Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.

Hint:
    The status here is the number of substring that end with each char in p
"""
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = [0] * 26
        end_with_cur = 0
        result = 0
        for i in range(len(p)):
            cur = ord(p[i]) - ord('a')
            if i > 0 and ord(p[i-1]) != (cur - 1) % 26 + ord('a'):
                end_with_cur = 0
            end_with_cur += 1
            if end_with_cur > dp[cur]:
                result += end_with_cur - dp[cur]
                dp[cur] = end_with_cur
        return result


if __name__ == "__main__":
    p = "zab"
    print(Solution().findSubstringInWraproundString(p))
