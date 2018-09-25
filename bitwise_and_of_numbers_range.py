"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0

"""

class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        times = 1
        while m != n:
            m >>= 1
            n >>= 1
            times <<= 1
        return m * times


if __name__ == "__main__":
    print(Solution().rangeBitwiseAnd(5, 7))
    print(Solution().rangeBitwiseAnd(0, 1))
