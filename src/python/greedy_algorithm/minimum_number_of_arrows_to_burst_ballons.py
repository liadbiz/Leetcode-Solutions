"""
There are a number of spherical balloons spread in two-dimensional space. For
each balloon, provided input is the start and end coordinates of the horizontal
diameter. Since it's horizontal, y-coordinates don't matter and hence the
x-coordinates of start and end of the diameter suffice. Start is always smaller
than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the
x-axis. A balloon with xstart and xend bursts by an arrow shot at x if
x_start ≤ x ≤ x_end. There is no limit to the number of arrows that can be shot.
An arrow once shot keeps travelling up infinitely. The problem is to find the 
minimum number of arrows that must be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
"""
class Solution:
    # 思路： 按照每个范围的start增序排序，然后遍历每个范围，找出符合题目意思的
    # 重叠区个数即可
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        points.sort(key=lambda x : x[0])
        res, low = 0, max(p[1] for p in points) + 1
        for p in points:
            low = min(p[1],low)
            if p[0] > low:
                res += 1
                low = p[1]
        return res + 1


if __name__ == '__main__':
    points = [[10,16], [2,8], [1,6], [7,12]]
    points2 = [[1, 2], [3,4], [5,6],[7,8]]
    print(Solution().findMinArrowShots(points))
    print(Solution().findMinArrowShots(points2))
