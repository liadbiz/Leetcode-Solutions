"""
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
"""
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False
        mask = 1
        while mask < n:
            mask <<= 1
        return True if  mask & n else False
    

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if n <= 0 else not n & (n - 1)

if __name__ == "__main__":
    print(Solution().isPowerOfTwo(1))
    print(Solution().isPowerOfTwo(16))
    print(Solution().isPowerOfTwo(218))
