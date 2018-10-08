"""
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.
Example 3:
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.
Example 4:
Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.
"""
class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n ^= n >> 2
        return not n & (n - 1)
        
    def hasAlternatingBits2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n ^= n >> 1
        return not n & (n + 1)

if __name__ == "__main__":
    num = 5
    print(Solution().hasAlternatingBits(num))
    num = 7
    print(Solution().hasAlternatingBits(num))
    num = 11
    print(Solution().hasAlternatingBits(num))
    num = 5
    print(Solution().hasAlternatingBits2(num))
    num = 7
    print(Solution().hasAlternatingBits2(num))
    num = 11
    print(Solution().hasAlternatingBits2(num))
