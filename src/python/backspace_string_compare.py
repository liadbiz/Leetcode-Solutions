"""

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""

class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        res = []
        for s in [S, T]:
            tmp = []
            for i in s:
                if i is not "#":
                    tmp.append(i)
                elif i is "#" and tmp != []:
                    tmp.pop()
            res.append(tmp)
        return res[0] == res[1]

    def backspaceCompare2(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))

if __name__ == "__main__":
    S1 = "ab#c"
    T1 = "ad#c"
    S2 = "ab##"
    T2 = "c#d#"
    S3 = "a##c"
    T3 = "#a#c"
    S4 = "a#c"
    T4 = "b"
    print(Solution().backspaceCompare(S1, T1))
    print(Solution().backspaceCompare(S2, T2))
    print(Solution().backspaceCompare(S3, T3))
    print(Solution().backspaceCompare(S4, T4))
    print(Solution().backspaceCompare2(S1, T1))
    print(Solution().backspaceCompare2(S2, T2))
    print(Solution().backspaceCompare2(S3, T3))
    print(Solution().backspaceCompare2(S4, T4))
