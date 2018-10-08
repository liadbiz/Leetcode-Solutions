# Time:  O(n^2)
# Space: O(1)
#
# Given an array S of n integers,
# find three integers in S such that the sum is
# closest to a given number, target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.
#
# For example, given array S = {-1 2 1 -4}, and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums, result, min_dis, i = sorted(nums), float("inf"), float("inf"), 0
        while i < len(nums) - 2:
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    dis = nums[i] + nums[j] + nums[k] - target
                    if abs(dis) < min_dis:
                        min_dis = abs(dis)
                        result = nums[i] + nums[j] + nums[k]
                    if dis < 0:
                        j += 1
                    elif dis > 0:
                        k -= 1
                    else:
                        return target
            i += 1
        return result


if __name__ == "__main__":
    result = Solution().threeSumClosest([-1, 2, 1, -4], 1)
    print("test [-1, 2, 1, -4]", end="\n")
    print(result, end="\n")
