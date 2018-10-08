"""
Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.

example 1:
input: 4
output: 2

example 2:
input 8
output 2
Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated.
"""

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        import math
        return math.trunc(math.sqrt(x))


"""
what have learned:

1. math.trunc(x) traunc decimal number.
2. math.sqrt(x) get squared root of x.
"""
        