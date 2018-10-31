"""
A sequence of numbers is called a wiggle sequence if the differences between
successive numbers strictly alternate between positive and negative. The first
difference (if one exists) may be either positive or negative. A sequence with
fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences
(6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5]
and [1,7,4,5,5] are not wiggle sequences, the first because its first two
differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that
is a wiggle sequence. A subsequence is obtained by deleting some number of
elements (eventually, also zero) from the original sequence, leaving the
remaining elements in their original order.

Example 1:

Input: [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.
Example 2:

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is
[1,17,10,13,10,16,8].
Example 3:

Input: [1,2,3,4,5,6,7,8,9]
Output: 2
Follow up:
Can you do it in O(n) time?

"""
class Solution:
    # 思路，首先去掉连续的相同的数，只保留一个就可以，这里用的是itertools.groupby
    # 函数，然后处理长度小于2的特例，然后求出difference列表，计算相邻difference异
    # 号的个数，加2返回即可。
    # 函数2是该思路的简化版，用nan避免单独处理特例的情况
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import itertools
        nums = [n for n, _ in itertools.groupby(nums)]
        if len(nums) < 2:
            return len(nums)
        subs_nums = [b - a for a , b in zip(nums, nums[1:])]
        return 2 + sum(a * b < 0 for a, b in zip(subs_nums, subs_nums[1:]))

    def wiggleMaxLength2(self, nums):
        nan = float('nan')
        diffs = [a-b for a, b in zip([nan] + nums, nums + [nan]) if a-b]
        return sum(d*e < 0 for d, e in zip(diffs, diffs[1:]))

if __name__ == '__main__':
    nums1 = [1,7,4,9,2,5]
    nums2 = [1,17,5,10,13,15,10,5,16,8]
    nums3 = [1,2,3,4,5,6,7,8,9]
    print(Solution().wiggleMaxLength(nums1))
    print(Solution().wiggleMaxLength(nums2))
    print(Solution().wiggleMaxLength(nums3))
    print(Solution().wiggleMaxLength2(nums1))
    print(Solution().wiggleMaxLength2(nums2))
    print(Solution().wiggleMaxLength2(nums3))

