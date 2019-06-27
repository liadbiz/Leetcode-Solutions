"""
#787 cheapest flights within k stops
source: https://leetcode-cn.com/problems/cheapest-flights-within-k-stops/

Hint: use bellman ford algorithm, but only run for K times.
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        inf = float('inf')
        dis = [inf] * n
        dis[src] = 0
        for _ in range(K + 1):
            dis_new = dis.copy()
            for s, d, p in flights:
                if dis[s] != inf and dis[s] + p < dis_new[d]:
                    dis_new[d] = dis[s] + p
            dis = dis_new.copy()
        return -1 if dis[dst] == inf else dis[dst]


if __name__ == "__main__":
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    K = 0
    assert Solution().findCheapestPrice(n, flights, src, dst, K) == 500, "result is not correct"
                    
