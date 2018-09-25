"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Example 1:

Input: 11
Output: 3
Explanation: Integer 11 has binary representation 00000000000000000000000000001011
Example 2:

Input: 128
Output: 1
Explanation: Integer 128 has binary representation 00000000000000000000000010000000
"""
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        mask = 1
        res = 0
        while mask <= n:
            if mask | n == n:
                res += 1
            mask <<= 1
        return res


    def hammingWeight2(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n != 0:
            n = n & (n - 1)
            res += 1
        return res


if __name__ == "__main__":
    n1 = 11
    n2 = 128
    print(Solution().hammingWeight(n1))
    print(Solution().hammingWeight(n2))
