class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        top = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        left = [str(index + 1) for index, item in enumerate(nums)][:3]
        return top + left
         
                                    
if __name__ == "__main__":
    print(Solution().findRelativeRanks(points))
