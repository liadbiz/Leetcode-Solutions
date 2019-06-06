"""
#304 Range Sum Query 2D - Immutable

source: https://leetcode.com/problems/range-sum-query-2d-immutable/
"""
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        self.matrix = matrix
        m = len(matrix)
        n = len(matrix[0])
        self.__sums = [[0] * (n+1) for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                self.__sums[i][j] = self.__sums[i][j-1] + matrix[i-1][j-1]
        for j in  range(1,n+1):
            for i in range(1, m+1):
                self.__sums[i][j] += self.__sums[i-1][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.__sums[row2+1][col2+1]-self.__sums[row1][col2+1] - \
                self.__sums[row2+1][col1] + self.__sums[row1][col1]

if __name__ == "__main__":
  matrix =  [
      [3, 0, 1, 4, 2],
      [5, 6, 3, 2, 1],
      [1, 2, 0, 1, 5],
      [4, 1, 0, 1, 7],
      [1, 0, 3, 0, 5]
      ]
  obj = NumMatrix(matrix)
  print(obj.sumRegion(2,1,3,4))
