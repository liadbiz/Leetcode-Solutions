"""
967. Numbers With Same Consecutive Differences
source: https://leetcode-cn.com/problems/numbers-with-same-consecutive-differences/

Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.

 

Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

"""
class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        res = set(range(10))
        for i in range(N - 1):
            new_res = set()
            for n in res:
                if n == 0:
                    continue
                last = n % 10
                if last + K <= 9:
                    new_res.add(10 * n  + last + K)
                if last - K >= 0:
                    new_res.add(10 * n  + last - K)
            res = new_res
        
        return sorted(list(res))
        
if __name__ == "__main__":
    N = 3
    K = 7
    result = [181, 292, 707, 818, 929]
    assert Solution().numsSameConsecDiff(N, K) == result, "result is not correct"

