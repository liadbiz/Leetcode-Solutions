import heapq
class Solution:
    # one dp method, but time exeeded
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [True]
        m = 1
        i = 2
        while m != n:
            if (not i % 2 and dp[i // 2 - 1]) or (not i % 3 and dp[i // 3 - 1]) or ( not i % 5 and dp[i // 5 - 1]):
                dp.append(True)
                result = i
                m += 1
            else:
                dp.append(False)
            i += 1
        print(dp[i - 2])
        return result

    # key point: only generate numbers you need
    def nthUglyNumber(self, n: int) -> int:
        ugly_number = 0

        heap = []
        heapq.heappush(heap, 1)
        for _ in range(n):
            ugly_number = heapq.heappop(heap)
            if ugly_number % 2 == 0:
                heapq.heappush(heap, ugly_number * 2)
            elif ugly_number % 3 == 0:
                heapq.heappush(heap, ugly_number * 2)
                heapq.heappush(heap, ugly_number * 3)
            else:
                heapq.heappush(heap, ugly_number * 2)
                heapq.heappush(heap, ugly_number * 3)
                heapq.heappush(heap, ugly_number * 5)

        return ugly_number
