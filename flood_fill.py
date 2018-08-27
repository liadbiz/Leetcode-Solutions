"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.


Idea:
    This is a typical exampel of DFS and BFS. We can use these two methods with
    recursive or iterative way.
"""

class Solution:
    def floodFill1(self, image, sr, sc, newColor): # DFS recursive
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        row, col = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r + 1 < row:
                    dfs(r + 1, c)
                if c + 1 < col:
                    dfs(r, c + 1)
                if r - 1 >= 0:
                    dfs(r - 1, c)
                if c - 1 >= 0:
                    dfs(r, c - 1)
        dfs(sr, sc)
        return image

    
    def floodFill2(self, image, sr, sc, newColor): # DFS iterative
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        row, col = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image
        import collections
        stack = collections.deque()
        stack.append((sr, sc))
        while stack:
            r, c = stack.pop()
            if image[r][c] == color:
                image[r][c] = newColor
                if r + 1 < row:
                    stack.append((r + 1, c))
                if c + 1 < col:
                    stack.append((r, c + 1))
                if r - 1 >= 0:
                    stack.append((r - 1, c))
                if c - 1 >= 0:
                    stack.append((r, c - 1))
        return image

    def floodFill3(self, image, sr, sc, newColor): # BFS iterative
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        row, col = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image
        import collections
        q = collections.deque()
        q.append((sr, sc))
        while q:
            r, c = q.pop()
            if image[r][c] == color:
                image[r][c] = newColor
                if r + 1 < row:
                    q.appendleft((r + 1, c))
                if c + 1 < col:
                    q.appendleft((r, c + 1))
                if r - 1 >= 0:
                    q.appendleft((r - 1, c))
                if c - 1 >= 0:
                    q.appendleft((r, c - 1))
        return image

if __name__ == "__main__":
    case1 = [[1,1,1],[1,1,0],[1,0,1]]
    pprint(Solution().floodFill1(case1))
    pprint(Solution().floodFill2(case1))
    pprint(Solution().floodFill3(case1))

