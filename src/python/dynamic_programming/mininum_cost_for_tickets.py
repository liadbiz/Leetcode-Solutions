"""
In a country popular for train travel, you have planned some train travelling
one year in advance.  The days of the year that you will travel is given as an
array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

+ a 1-day pass is sold for costs[0] dollars;
+ a 7-day pass is sold for costs[1] dollars;
+ a 30-day pass is sold for costs[2] dollars.

The passes allow that many days of consecutive travel.  For example, if we
get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5,
6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the
given list of days.

problem source: https://leetcode.com/problems/minimum-cost-for-tickets/
"""
from functools import lru_cache
class Solution:
    # complexity: O(365)
    # space: O(365)
    # dp via days
    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':
        days = set(days)
        durations = [1, 7, 30]
        # return the cost of traveling from day d to 365
        def dp(i):
            if i > 365:
                return 0
            elif i in days:
                return min(dp(i + d) + c for c, d in zip(costs, durations))
            else:
                return dp(i + 1)
        return dp(1)
        
    # complexity: O(N)
    # space: O(N) 
    # N is the length of `days`
    # dp via window
    def mincostTickets2(self, days: 'List[int]', costs: 'List[int]') -> 'int':
        durations = [1, 7, 30]
        N = len(days)
        def dp(i):
            if i >= N:
                return 0
            res = float('inf')
            j = i
            for c, d in zip(costs, durations):
                while j < N and days[j] < days[i] + d:
                    j += 1
                res = min(res, c+dp(j))
            return res 
        return dp(0)

if __name__ == "__main__":
    days =[1,4,6,7,8,20]
    costs = [2, 7, 15]
    days2 = [1,2,3,4,5,6,7,8,9,10,30,31]
    costs2= [2,7,15]
    print(Solution().mincostTickets(days, costs))
    print(Solution().mincostTickets(days2, costs2))
    print(Solution().mincostTickets2(days, costs))
    print(Solution().mincostTickets2(days2, costs2))
                    
