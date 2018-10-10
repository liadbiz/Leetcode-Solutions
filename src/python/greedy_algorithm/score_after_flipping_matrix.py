"""
We have a two dimensional matrix A where each value is 0 or 1.

A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.

After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score.

 

Example 1:

Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation:
Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
 

Note:

1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] is 0 or 1.
"""

class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        flag = True
        while flag:
            flag = False
            # togging rows
            for index, row in enumerate(A):
                row_ = [1 if i == 0 else 0 for i in row]
                if int(''.join(str(i) for i in row_), 2) > int(''.join(str(i)
                    for i in row), 2):
                    A[index] = row_
                    flag = True

            # togging columns
            for i in range(len(A[0])):
                col = [A[r][i] for  r in range(len(A))]
                col_ = [1 if i == 0 else 0 for i in col]
                if col_.count(1) > col.count(1):
                    for r in range(len(A)):
                        A[r][i] = col_[r]
                    flag = True
        return sum(int(''.join(str(i) for i in row), 2) for row in A)
    
    def matrixScore2(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        r = len(A)  # row lenth
        c = len(A[0]) # column length
        res = (1 <<(c - 1)) * r # every first item of each row should be 1
        for j in range(1, c):
            num = sum(A[i][j] == A[i][0] for i in range(r))
            res += max(r - num, num) * (1 << (c - j - 1))
        return res


if __name__ == "__main__":
    A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
    print(Solution().matrixScore(A))
    print(Solution().matrixScore2(A))
