"""
A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.

Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two (axis-aligned) rectangles, return whether they overlap.

Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
Notes:

Both rectangles rec1 and rec2 are lists of 4 integers.
All coordinates in rectangles will be between -10^9 and 10^9.

Main Idea:
    It is easier to think this problem from the opposite direction. There are
    only four cases that two rectangle is not overlapped. They are:
    + rec1 is left to the rec2
    + rec1 is right to the rec2
    + rec1 is higher than rec2
    + rec1 is lower than rec2
"""

class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return not (rec1[2] <= rec2[0] or
                    rec2[2] <= rec1[0] or
                    rec2[3] <= rec1[1] or
                    rec1[3] <= rec2[1])


if __name__ == "__main__":
    rec11 = [0,0,2,2]
    rec21 = [1,1,3,3]
    rec12 = [0,0,1,1]
    rec22 = [1,0,2,1]
    print(Solution().isRectangleOverlap(rec11, rec21))
    print(Solution().isRectangleOverlap(rec12, rec22))
