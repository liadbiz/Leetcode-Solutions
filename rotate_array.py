class Solution(object):
    def rotate_array(self, nums, k):
        n = len(nums)
        k = k % n
        p = n - k
        for i in range(p // 2):
            temp = nums[i]
            nums[i] = nums[p - i - 1]
            nums[p - i - 1] = temp
        for i in range(p, (p + n) // 2):
            temp = nums[i]
            nums[i] = nums[p + n - i - 1]
            nums[p + n - i - 1] = temp
        for i in range(len(nums) // 2):
            temp = nums[i]
            nums[i] = nums[n - i - 1]
            nums[n - i - 1] = temp
        return nums


if __name__ == "__main__":
    print(Solution().rotate_array([1, 2, 3, 4, 5, 6, 7], 3))
    print(Solution().rotate_array([1, 2, 3, 4, 5, 6, 7], 11))
    print(Solution().rotate_array([1], 0))
