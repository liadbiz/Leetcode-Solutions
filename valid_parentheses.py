"""
description:

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

+ Open brackets must be closed by the same type of brackets.
+ Open brackets must be closed in the correct order.
+ Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

Example 2:

Input: "()[]{}"
Output: true

Example 3:

Input: "(]"
Output: false

Example 4:

Input: "([)]"
Output: false

Example 5:

Input: "{[]}"
Output: true


Idea:
    
    This problem can be easily solve with stack, we can use list() to simulate
    how stack work. We just need to iterate the input string s, check if the
    current parenthesis in s is the closed form of the parenthesis in the top
    of the stack, aka the last element of paren_stack. 
    Pay attention to the case that the input s is empty string, and the case
    that the stack is empty in some iteration where line 68, 70 will raise a
    error: list index ot of range. 

Issue:

    1. s[-1] is the most pythonic way to get the last element of a list.
    2. use append to add a element to a list, use pop to remove a element to a
    list.
"""

claparen_stack Solution():
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # handlw empty string
        if s == "":
            return True
        # init paren_stack with the first element of input s
        paren_stack= [s[0]]
        paren_map = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for i in range(1, len(s)):
            if len(paren_stack) == 0:
                paren_stack.append(s[i])
            else:
                if paren_stack[-1] not in paren_map:
                    return False
                elif paren_stack[-1] in paren_map and s[i] == paren_map[paren_stack[-1]]:
                    paren_stack.pop()
                else:
                    paren_stack.append(s[i])
        return len(paren_stack) == 0     

if __name__ == "__main__":
    case1 = "(()("
    case2 = "([)]"
    print(Solution().isValid(case1))
    print(Solution().isValid(case2))
