"""
Given a non-negative integer N, find the largest number that is less than or 
equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair
of adjacent digits x and y satisfy x <= y.)

Example 1:
Input: N = 10
Output: 9
Example 2:
Input: N = 1234
Output: 1234
Example 3:
Input: N = 332
Output: 299
Note: N is an integer in the range [0, 10^9].
"""
class Solution:
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        nums = list(map(int, list(str(N))))
        di = len(nums)
        for i in reversed(range(len(nums) - 1)):
            if nums[i] > nums[i + 1]:
                nums[i] -= 1
                di = i + 1
        for i in range(di, len(nums)):
            nums[i] = 9
        return int("".join(map(str, nums)))

if __name__ == '__main__':
    N1 = 10
    N2 =1234
    N3 = 332
    print(Solution().monotoneIncreasingDigits(N1))
    print(Solution().monotoneIncreasingDigits(N2))
    print(Solution().monotoneIncreasingDigits(N3))
