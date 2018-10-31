"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.
Example 1:

Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
Example 2:

Input: 
gas  = [2,3,4]
cost = [3,4,3]

Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
"""
class Solution:
    # 思路：函数一是我第一想到的思路，但是复杂度比较高，在最坏的情况下是O(N)，所以
    # 提交的时候有的测试用例会超时。函数二才是正确的思路，我们只需要遍历一次gas和
    # 即可，每次对当前gas和cost的值的差求和，如果当前小于0，说明在这之前的点开始都
    # 不行，那么把start置为下一个点即可。遍历结束如果总的和大于0，就返回start，否则
    # 返回-1
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        inds = [i for i, (a, b) in enumerate(zip(gas, cost)) if a - b >= 0]
        for i in inds:
            com = zip(gas[i:] + gas[:i], cost[i:] + cost[:i])
            s = 0
            for a, b in com:
                s += a - b
                if s < 0:
                    break
            else:
                return i
        else:
            return -1
                
            
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start, crt_sum, total_sum = 0, 0, 0
        for i in range(len(gas)):
            df = gas[i] - cost[i]
            crt_sum += df
            total_sum += df
            if crt_sum < 0:
                crt_sum = 0
                start = i + 1
        if total_sum >= 0:
            return start
        return -1


if __name__ == "__main__":
    gas1  = [1,2,3,4,5]
    cost1 = [3,4,5,1,2]
    gas2  = [2,3,4]
    cost2 = [3,4,3]
    print(Solution().canCompleteCircuit(gas1, cost1)) 
    print(Solution().canCompleteCircuit(gas2, cost2)) 
