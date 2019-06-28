"""
#801 Minimum Swaps To Make Sequences Increasing
source: https://leetcode-cn.com/problems/minimum-swaps-to-make-sequences-increasing/

We have two integer sequences A and B of the same non-zero length.

We are allowed to swap elements A[i] and B[i].  Note that both elements are in the same index position in their respective sequences.

At the end of some number of swaps, A and B are both strictly increasing.  (A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)

Given A and B, return the minimum number of swaps to make both sequences strictly increasing.  It is guaranteed that the given input always makes it possible.

Example:
Input: A = [1,3,5,4], B = [1,2,3,7]
Output: 1
Explanation:
Swap A[3] and B[3].  Then the sequences are:
A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
which are both strictly increasing.

Hint: The keypoint of this problem is to understand that it must have a solution.
and for each position, you have two choices, swap or not swap. 

+ if you swap when you must swap, swap times in this location equals to the swap times in previous location when you do not swap plus one.
+ if you do not swap when you must swap, swap times in this location equals to the swap times in prevous location when you swap.
+ if you swap when you must not swap, swap times in this location equals to the swap times in previous location when you swap plus one.
+ if you do not swap when you must not swap, swap times in this location equals to the swap times in previous location when you do not swap.
+ if you swap when you can swap or not, swap times in this location equals to the minimum swap times in previous location plus one.
+ if you do not swap when you can swap or not, swap times in this location equals to the minimum swap times in previous location.
"""

class Solution(object):
    def minSwap(self, A, B):
        cost = [0 ,1]
        for i in range(1, len(A)):
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                if A[i] > B[i - 1] and B[i] > A[i - 1]:
                    #cost = [min(cost), min(cost) + 1]
                    cost[0], cost[1] = min(cost), min(cost) + 1
                else:
                    cost[1] += 1
            else:
                # cost = [cost[1], cost[0] + 1]
                cost[0], cost[1] = cost[1], cost[0] + 1
        return min(cost)

    def minSwap2(self, A, B):
        dp_no_swap, dp_swap = [0]*2, [1]*2
        for i in xrange(1, len(A)):
            dp_no_swap[i%2], dp_swap[i%2] = float("inf"), float("inf")
            if A[i-1] < A[i] and B[i-1] < B[i]:
                dp_no_swap[i%2] = min(dp_no_swap[i%2], dp_no_swap[(i-1)%2])
                dp_swap[i%2] = min(dp_swap[i%2], dp_swap[(i-1)%2]+1)
            if A[i-1] < B[i] and B[i-1] < A[i]:
                dp_no_swap[i%2] = min(dp_no_swap[i%2], dp_swap[(i-1)%2])
                dp_swap[i%2] = min(dp_swap[i%2], dp_no_swap[(i-1)%2]+1)
        return min(dp_no_swap[(len(A)-1)%2], dp_swap[(len(A)-1)%2])


if __name__ == "__main__":
    A = [0, 4, 4, 5, 9]
    B = [0, 1, 6, 8, 10]
    assert Solution().minSwap(A, B) == 1, "result is not correct"
