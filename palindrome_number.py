# description
""" 
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.


Example 1:

Input: 121
Output: true

Example 2:

Input: -121
Output: false

Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: 10
Output: false

Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
""" 


class Solution:
    # a gentle solution
    def isPalindrome(self, x):
        if x >= 0:
            reverse_x = int(''.join([i for i in reversed(str(x))])) 
            if reverse_x == x:
               return True
        return False
    
    # a more concise solution
    def isPalindrome2(self, x):
        return str(x) == str(x)[::-1]


if __name__ == '__main__':
   print(Solution().isPalindrome(121))
   print(Solution().isPalindrome(10))
   print(Solution().isPalindrome(-121))
