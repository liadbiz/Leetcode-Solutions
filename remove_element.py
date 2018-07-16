"""
description:

Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

Idea:
    The idea is easy, remove the element in nums that equals to val.
    If you want to keep the order of the remaining element, The solution is
    like the first function. 
    But this problem do not expects the order, so we can use the second
    function.
    If you want to solve this problem with pythonic way, just use function 3
    which is nothing about algorithm.

"""


class Solution:
    def removeElement1(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, j = 0, 0
        # find the first val in nums
        while nums[i] != val:
            i += 1
            j += 1
        while j != len(nums):
            print(i, j)
            while nums[j] == val:
                j += 1
                if j == len(nums):
                    return i
            nums[i] = nums[j]
            i += 1
            j += 1
        return i


    def removeElement2(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] == val and nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            elif nums[i] != val:
                i += 1
            elif nums[j] == val:
                j -= 1
        return i

    def removeElement3(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while(val in nums):
    	    del nums[nums.index(val)]
        return len(nums)

if __name__ == '__main__':
    case1 = [3, 2, 2, 3]
    case2 = [0, 1, 2, 2, 3, 0, 4, 2]
    print(Solution().removeElement(case1, 3))
    print(Solution().removeElement(case2, 2))
