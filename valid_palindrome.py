class Solution(object):
    def isPalindrome(self, s):
        if s == '':
            return True
        left, right = 0, len(s) - 1
        while left < right:
            while not s[left].isalpha() and not s[left].isdigit():
                left += 1
                if left == right:
                    return True
            while not s[right].isalpha() and not s[right].isdigit():
                right -= 1
                if left == right:
                    return True
            if s[left] != s[right] and s[left].upper() != s[right].upper():
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
    print(Solution().isPalindrome("race a car"))
    print(Solution().isPalindrome(",."))
    print(Solution().isPalindrome("a."))
    print(Solution().isPalindrome("0p"))
