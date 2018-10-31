"""
N couples sit in 2N seats arranged in a row and want to hold hands. We want to know the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

Example 1:

Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
Example 2:

Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.
Note:

len(row) is even and in the range of [4, 60].
row is guaranteed to be a permutation of 0...len(row)-1.
"""
class Solution:
    # 思路：
    # 从[这篇博客](http://wowaccepted.com/2018/02/10/leetcode-765-couples-holding-hands%E9%A2%98%E7%9B%AE%E8%A7%A3%E6%9E%90-wowac/)中发现，最少的交换次数是每个圈的顶点个数之和减去圈的个数，怎么定义圈可以参考该博客，那么要做的就是如何找出圈的顶点个数以及圈的个数。时间复杂度和空间复杂度都是O(n)。一定程度上体现了贪心法的思想。每一次交换可以使一对couple或者两队可以相邻，如果不能使任何一对couple相邻，那么这个交换就没有意义，而圈的定义是统一这两种比较优的情况。
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        # find circles
        par = [i + 1 if i % 2 == 0 else i - 1 for i in range(len(row))]
        pos = [i for index in range(len(row)) for i, r in enumerate(row) if
                index == r]
        par_pos = [pos[i] for i in par] # pos of one's parterner
        visited = [0 for i in range(len(row))]
        res = 0
        for r in row:
            if not visited[pos[r]]:
                t = 0
                tmp = pos[r]
                while not visited[tmp]:
                    visited[tmp], visited[par[tmp]] = 1, 1
                    t += 1
                    tmp = par_pos[row[par[tmp]]]
                res += t - 1
        return res

                    
                    
if __name__ == "__main__":
    row1 = [0, 2, 1, 3]
    row2 = [0, 3, 4, 1, 2, 5, 6, 8, 7, 9]
    row3 = [3, 2, 0, 1]
    print(Solution().minSwapsCouples(row1))
    print(Solution().minSwapsCouples(row2))
    print(Solution().minSwapsCouples(row3))
