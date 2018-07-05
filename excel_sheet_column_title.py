class Solution(object):
    def convertToTitle(self, n):
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                   'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                   'Y', 'Z']
        digits = []
        while n > 0:
            digits.append(n % 26)
            if n % 26 == 0:
                n = n // 26 - 1
            else:
                n = n // 26
        result = ''
        for i in range(len(digits)):
            # print(digits[i])
            # print(letters[digits[i] - 1])
            result = letters[digits[i] - 1] + result
            # print(result)
        return result


if __name__ == "__main__":
    print(Solution().convertToTitle(26))
    print(Solution().convertToTitle(29))
    print(Solution().convertToTitle(52))
