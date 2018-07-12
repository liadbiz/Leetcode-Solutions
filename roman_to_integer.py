"""
problem url: https://leetcode.com/problems/roman-to-integer/description/

Wrong ideas:
    At the first glance, we may want to devide the problem into two cases, if
    the input string is one of those special cases. we just need to return the
    correpond number. And if not, we only need to sum all the integers that
    each roman character of input string correpond to. This idea dose not
    consider the case that if the special cases occurs in the input string.

Right idea:
    the right idea is:  THe difference between special case and normal case is
    that if the number current roman char represent is smaller than the next, we
    need to substract tthe current number, and if not, add the current
    number. When we finish iterating all the roman chars of input string, the
    sum is the number it represents.
""" 

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numbers_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        ss = [numbers_map[i] for i in s]
        number = 0
        l = len(s)
        for i in range(l - 1):
            if ss[i] >= ss[i + 1]:
                number += ss[i]
            elif ss[i] < ss[i + 1]:
                number -= ss[i]
        number += ss[l - 1]
        return number
        
if __name__ == '__main__':
    print("Example 1: \n")
    print("Input: III \nOutput: ")
    print(Solution().romanToInt('III'), '\n')
    print("Example 2: \n")
    print("Input: IV \nOutput: ")
    print(Solution().romanToInt('IV'), '\n')
    print("Example 3: \n")
    print("Input: IX \nOutput: ")
    print(Solution().romanToInt('IX'), '\n')
    print("Example 4: \n")
    print("Input: MCMXCIV \nOutput: ")
    print(Solution().romanToInt('MCMXCIV'), '\n')
