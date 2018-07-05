class Solution(object):
    def valid_palindrome(self, s):
        times = 0
        for i in range(len(s) // 2):
            if times > 1:
                print("case 0")
                return False
            if s[i] != s[len(s) - i - 1] and s[i] == s[len(s) - i - 2]:
                print("first case")
                times += 1
            elif s[i] != s[len(s) - i - 1] and s[i + 1] == s[len(s) - i - 1]:
                print("second case")
                times += 1
                i += 1
            elif s[i] != s[len(s) - i - 1] and s[i] != s[len(s) - i  - 2]:
                print("case 1")
                return False
            elif s[i] != s[len(s) - i - 1] and s[i + 1] != s[len(s) - i - 1]:
                print("case 1")
                return False
        return True


if __name__ == "__main__":
    print(Solution().valid_palindrome("abca"))
    print(Solution().valid_palindrome("abcca"))
    print(Solution().valid_palindrome("deeee"))
    print(Solution().valid_palindrome("hbakab"))
