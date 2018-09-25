"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?

"""
class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        mask = 1
        while mask < num:
            mask <<= 2
        return True if  mask & num else False

    def isPowerOfFour2(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return True if num > 0 and not num & (num - 1) and num & 0x55555555 else False

if __name__ == "__main__":
    print(Solution().isPowerOfFour(1))
    print(Solution().isPowerOfFour(16))
    print(Solution().isPowerOfFour(218))

    print(Solution().isPowerOfFour2(1))
    print(Solution().isPowerOfFour2(16))
    print(Solution().isPowerOfFour2(218))

