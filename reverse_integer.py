"""
Given a 32-bit signed integer, reverse digits of an integer.

Example1: 

Input: 123
output: 321

Example2:

Input: -123
Output: -321

Example3:

Input: 120
Output: 21

Notes: what if the result overflow?

what have learned:

1. in python 2, we can use cmp() function to get sign of the difference of two number a and b, in python 3, we can use (a > b) - (a < b)
2. str() function: int number to string

"""

class Solution:
    def reverse1(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0;
            return -self.reverse1(-x)
        result = 0
        while x:
            result = result * 10 + x % 10
            x //= 10
        return result if result  < 2 ** 31 else 0 

    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = (x > 0) - (0 < x)
        r = int(str(s * x)[::-1])
        return s * r * (r < 2**31)

