"""
An integer interval [a, b] (for integers a < b) is a set of all consecutive
integers from a to b, including a and b.

Find the minimum size of a set S such that for every integer interval A in
intervals, the intersection of S with A has size at least 2.

Example 1:
Input: intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
Output: 3
Explanation:
Consider the set S = {2, 3, 4}.  For each interval, there are at least 2
elements from S in the interval.
Also, there isn't a smaller size set that fulfills the above condition.
Thus, we output the size of this set, which is 3.
Example 2:
Input: intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
Output: 5
Explanation:
An example of a minimum sized set is {1, 2, 3, 4, 5}.
Note:

intervals will have length in range [1, 3000].
intervals[i] will have length 2, representing some integer interval.
intervals[i][j] will be an integer in [0, 10^8].
"""
class Solution:
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        r = [float('-inf')] * 2
        res = 0
        for l, h in sorted(intervals, key=lambda x:x[1]):
            if r[0] < l <= r[1]:
                res += 1
                r = r[1], h
            elif l > r[1]:
                res += 2
                r = h - 1, h
        return res


if __name__ == '__main__':
    intervals1 = [[1, 3], [1, 4], [2, 5], [3, 5]]
    intervals2 = [[1, 2], [2, 3], [2, 4], [4, 5]]
    intervals3 = [[1, 5]]
    intervals4 = [[4,14],[6,17],[7,14],[14,21],[4,7]]
    intervals5 = [[33,44],[42,43],[13,37],[24,33],[24,33],[25,48],[10,47],[18,24],[29,37],[7,34]]
    print(Solution().intersectionSizeTwo(intervals1))
    print(Solution().intersectionSizeTwo(intervals2))
    print(Solution().intersectionSizeTwo(intervals3))
    print(Solution().intersectionSizeTwo(intervals4))
    print(Solution().intersectionSizeTwo(intervals5))
