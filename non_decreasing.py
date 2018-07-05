class Solution(object):
    # Brute force
    def checkPossibility2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
    # Reduce to maller problem

    # locate and analyze index
    def checkPossibility3(self, nums):
        p = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                p = i           # find a problem index
        return (p is None or p == 0 or p == len(nums) - 2
                or nums[p - 1] < nums[p + 1] or nums[p] < nums[p + 2])


if __name__ == "__main__":
    print(Solution().checkPossibility3([-1, 4, 2, 3]))
