"""
description:

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # recursive
        if n == 1:
            return "1"
        previous = self.countAndSay(n - 1)
        i, j = 0, 0
        now = ""
        while i < len(previous):
            while previous[j] == previous[i]:
                j += 1
                if j >= len(previous):
                    break
            if (j - i) > 0:
                now += str(j - i) + previous[i]
                i = j
            elif (j - i) == 0:
                now += str(1) + previous[i]
                j += 1
                i += 1
        return now
    
if __name__ == '__main__':
    print(Solution().countAndSay(3))
    print(Solution().countAndSay(4))
    print(Solution().countAndSay(5))
    print(Solution().countAndSay(6))
