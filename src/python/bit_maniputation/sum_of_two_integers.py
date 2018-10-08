"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1
"""
class Solution(object):
    def getSum(self, a, b):
        print(a, b)
        return a if b == 0 else self.getSum(a^b, (a&b)<<1)


    def getSum2(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32位能表示的最大整数(2147483647)
        MAX = 0x7FFFFFFF
        # 32位能表示的最小负数(-2147483648)
        # MIN = 0x80000000
        # 用来获取最低32位的掩码，此题的测试用例应该都是32位整数
        mask = 0xFFFFFFFF
        while b:
            # 只取32位保证循环可以结束，处理溢出的情况
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
            print(a, b)
        # 最后 ~(a ^ mask)这一步是为了纠正结果为负数的情况
        return a if a <= MAX else ~(a ^ mask)

if __name__ == "__main__":
    # test algorithm 1
    # print(Solution().getSum(2, 3))
    # print(Solution().getSum(2, -3))
    # print(Solution().getSum(-2, -3))
    print(Solution().getSum(-2147483646, -2147483647))
    # print(Solution().getSum(-2147483646, 2147483647))
    # test algorithm 2
    # print(Solution().getSum2(2, 3))
    # print(Solution().getSum2(2, -3))
    # print(Solution().getSum2(-2, -3))
    # 这个测试的结果也不对，说明这个解法也是不完善的，只是可以ac而已。
    # print(Solution().getSum2(-2147483646, -2147483647)) 
    # print(Solution().getSum2(-2147483646, 2147483647))

