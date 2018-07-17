class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # step 1, get the skyline from top/bottom, left/right
        column_len = len(grid[0])
        row_len    = len(grid)
        skyline_lr = [max(row) for row in grid]
        skyline_tb = []
        for i in range(column_len):
            skyline_tb.append(max([row[i] for row in grid]))
        
        # step 2, construct gridNew from skyline_lr and skyline_tb
        sum = 0
        for i in range(len(skyline_lr)):
            sum += sum([skyline_lr[i] - grid[i][j] if skyline_lr[i] < skyline_tb[j] else skyline_tb[j] - grid[i][j] for j in range(len(skyline_tb))])
        return sum 