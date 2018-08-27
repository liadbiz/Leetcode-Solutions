# question description:
#
# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#


class Solution:
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        bruce force: iterate two timesto find two numbers that match
        space: O(1)
        time: O(n^2)
        """
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[(i + 1):]):
                if x + y == target:
                    return [i, j + i + 1]
        return []

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        use hash map to store value and index of nums
        space: O(n)
        time: O(n)
        """
        cache = {}
        for i, num in enumerate(nums):
            cache[num] = i
        for i, num in enumerate(nums):
            if target - num in cache:
                if i < cache[target - num]:
                    return [i, cache[target - num]]
                elif i > cache[target - num]:
                    return [cache[target - num], i]
        return []

    def twoSum3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        iterate once to speed key, value cache
        space: O(n)
        time: O(n)
        """
        result = {}
        for i, num in enumerate(nums):
            if target - num in result:
                return [result[target - num], i]
            result[num] = i
        return []

    def twoSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        same as twoSum1 
        """
        k = 0
        for i in nums:
            j = target - i
            k += 1
            tmp_nums = nums[k:]
            if j in tmp_nums:
                return [k - 1, tmp_nums.index(j) + k]
        return []


if __name__ == '__main__':
    print("test case: [2, 7, 11, 15]", end="\n")
    print(Solution().twoSum1([2, 7, 11, 15], 9), end='\n')
    print(Solution().twoSum2([2, 7, 11, 15], 9), end='\n')
    print(Solution().twoSum3([2, 7, 11, 15], 9), end='\n')
    print(Solution().twoSum4([2, 7, 11, 15], 9), end='\n')

    print("test case: [3, 6, 3, 15]", end="\n")
    print(Solution().twoSum1([3, 6, 3, 15], 6), end='\n')
    print(Solution().twoSum2([3, 6, 3, 15], 6), end='\n')
    print(Solution().twoSum3([3, 6, 3, 15], 6), end='\n')
    print(Solution().twoSum4([3, 6, 3, 15], 6), end='\n')
