"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two
             conditions.
"""
class Solution:
    # 思路：对于每个人，只需要考虑她邻居是否比他大，只需要保证她的candy的数量比她的
    # 邻居中rating值比她小的那个的糖果要多一个就行了，如果两个邻居都比她小，那么取
    # 更大的candy加一即可。这里用正反两个方向遍历可以实现这个思路。
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        import operator
        from functools import reduce
        candy = [1 for _ in ratings]
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                candy[i] = candy[i - 1] + 1
        for i in reversed(range(1, len(ratings))):
            if ratings[i - 1] > ratings[i] and candy[i - 1] <= candy[i]:
                candy[i - 1] = candy[i] + 1
        return reduce(operator.add, candy)

if __name__ == "__main__":
    ratings1 = [1, 0, 2]
    ratings2 = [1, 2, 2]
    print(Solution().candy(ratings1))
    print(Solution().candy(ratings2))
