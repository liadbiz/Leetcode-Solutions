"""
#1049. Last Stone Weight II
source: https://leetcode-cn.com/problems/last-stone-weight-ii/submissions/

We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose any two rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the smallest possible weight of this stone (the weight is 0 if there are no stones left.)

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We can combine 2 and 4 to get 2 so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1 so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0 so the array converts to [1] then that's the optimal value.

Hint:
    split stones into two part, and the weights of all stones in one part is no more than `sum(stones) // 2`
    And find the solution that make the weights is biggest, then the smallest stone weight is the difference of
    the weights in these two part.
    You can find the solution by using 0-1 backpack trick.
    max weight of backpack: `sum(stones) // 2`
    weight array: stones
    value array: stones
"""
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sum_weight = sum(stones)
        half_weight = sum_weight // 2
        dp = [0 for i in range(half_weight + 1)]
        n = len(stones)
        for i in range(n):
            for j in range(half_weight, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]] + stones[i])
        return sum_weight - 2 * dp[half_weight]

if __name__ == "__main__":
    stones = [2, 7, 4, 1, 8, 1]
    print(Solution().lastStoneWeightII(stones))
