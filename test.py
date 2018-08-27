class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(range(len(nums) + 1)) - sum(nums)
         
                                    
if __name__ == "__main__":
    nums = [9,6,4,2,3,5,7,0,1]
    print(Solution().missingNumber(nums))
