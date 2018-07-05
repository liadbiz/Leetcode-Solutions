class Solution(object):
    def countPrimes(self, n):
        import math
        flags = []
        for i in range(n):
            flags.append(True)
        for i in range(2, int(math.sqrt(n)) + 1):
            if flags[i]:
                p = 2
                while p * i < n:
                    flags[p * i] = False
                    p += 1
        count = 0
        for i in range(2, n):
            if flags[i]:
                count += 1
        return count


if __name__ == "__main__":
    print(Solution().countPrimes(5))
    print(Solution().countPrimes(10))
