class Solution(object):
    def largest_opwer(self, n):
        n = n | n >> 1
        print(n)
        n = n | n >> 2
        print(n)
        n = n | n >> 4
        print(n)
        n = n | n >> 8
        print(n)
        n = n | n >> 16
        print(n)
        return (n + 1) >> 1

if __name__ == "__main__":
    print(Solution().largest_opwer(9))
