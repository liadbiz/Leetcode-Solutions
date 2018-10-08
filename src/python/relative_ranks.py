"""
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.

"""

class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        import operator
        nums_with_index = [(index, item) for index, item in enumerate(nums)]
        nums_with_index.sort(reverse=True, key=operator.itemgetter(1))
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for index, item in enumerate(nums_with_index[:3]):
            nums[item[0]] = medals[index]
        for index, item in enumerate(nums_with_index[3:]):
            nums[item[0]] = str(index + 4)
        return nums
    

if __name__ == "__main__":
    nums = [5,2,1,3,4]
    print(Solution().findRelativeRanks(nums))
