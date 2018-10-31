"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing
which is 0.
"""
class Solution:
    # 思路：依次遍历num，维护一个列表out，里面保存的是当前遍历过的digit能组成的最小
    # 的数，如果当前遍历的digit比out中最后一个digti小，就用该digit替换之，否则直接
    # 添加到out中。遍历结束后，如果k不为0，说明out中最后k个digit是多余的。
    # 注意out[:k or None]这种写法技巧。 即out[:None] = out
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        out = []
        for d in num:
            while k and out and out[-1] > d:
                out.pop()
                k -= 1
            out.append(d)
        return ''.join(out[:-k or None]).lstrip('0') or '0'

if __name__ == "__main__":
    num1 = "1432219"
    k1 = 2
    num2 = "10200"
    k2 = 1
    num3 = "10"
    k3 = 2
    print(Solution().removeKdigits(num1, k1))
    print(Solution().removeKdigits(num2, k2))
    print(Solution().removeKdigits(num3, k3))
