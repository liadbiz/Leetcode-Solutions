class Solution(object):
    def reverse_number(self, number):
        tag = True
        if number < 0:
            number = -number
            tag = False
        digits = []
        while number > 0:
            digits.append(number % 10)
            number = number // 10
        result = 0
        for i in range(len(digits)):
            result = result * 10 + digits[i]
        if result > 2 ** 31:
            return 0
        elif tag is False:
            return -result
        else:
            return result


if __name__ == "__main__":
    print(Solution().reverse_number(123))
    print(Solution().reverse_number(130))
    print(Solution().reverse_number(1000000003))
