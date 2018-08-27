"""
In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.



Example 1:

Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
Example 2:

Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.
Example 3:

Input: "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
"""

class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        i = 0
        now = ""
        count = 1
        res = []
        start, end = 0, 0
        while i <= len(S) - 1:
            if S[i] != now:
                if count >= 3:
                    res.append([start, end])
                start, end = i, i
                count = 1
                now = S[i]
            else:
                end = i
                count += 1
            i += 1
        if count >= 3:
            res.append([start, end])
        return res


if __name__ == "__main__":
    S1 = "abbxxxxzzy"
    S2 = "abc"
    S3 = "abcdddeeeeaabbbcd"
    S4 = "aaa"
    S5 = "aa"
    print(Solution().largeGroupPositions(S1))
    print(Solution().largeGroupPositions(S2))
    print(Solution().largeGroupPositions(S3))
    print(Solution().largeGroupPositions(S4))
    print(Solution().largeGroupPositions(S5))
