class Solution(object):
    def firsBadVersion(self, n):
        min = 1
        max = n
        while max > min:
            mid = (min + max) // 2
            if isBadVersion(mid):
                max = mid
            else:
                min = mid + 1
        return min
