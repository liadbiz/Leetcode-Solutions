class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9
        max = (10 ** n - 1) ** 2
        min = (10 ** (n - 1)) ** 2
        n = max
        while n >= min:
            if self.isPalindrome(n):
                return n / 1337

    def isPalindrome(self, n):
        values = []
        while n != 0:
            values .append(n % 10)
            n = n / 10
        length = len(values)
        for i in range(int(length / 2)):
            if values[i] != values[length - 1 - i]:
                return False
        return True


if __name__ == "__main__":
    print(Solution().largestPalindrome(2))
