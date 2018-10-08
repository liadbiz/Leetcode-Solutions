"""
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.

Key Idea:

We dont need to find which two num that can get the maximum xor result，
actually, we only need to find that maximum result.

We can find the result bit by bit. That is: suppose we have got the first
k bit of the result, how to find the k + 1 bits of the result? We will use
a property of ^ operator.

If a ^ b = c, then a ^ c = b, and b ^ c = a

So if there are two k + 1 bits prefix num from nums that can make the (k + 1)
be 1, then add 1 to the (k + 1)th bit, otherwise, add 0.

"""
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32)[::-1]:
            res <<= 1
            tmp = {num >> i for num in nums}
            res += any([res ^ 1 ^ t in tmp for t in tmp])
        return res


if __name__ == '__main__':
    nums = [3, 10, 5, 25, 2, 8]
    print(Solution().findMaximumXOR(nums))
