"""
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
Example 2:

Input: "cbacdcbc"
Output: "acdb"
"""
class Solution:
    # 思路：找出右侧包含所有s中字符的最小坐标，然后在其左侧找出字母表中最小的，然后
    # 将该字母右侧部分将该字母去掉之后的字符串置为s，知道s为空。
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        while s:
            li =  min(map(s.rindex, set(s)))
            c = min(s[:li + 1])
            res += c
            s = s[s.index(c):].replace(c, '')
        return res
        
if __name__ == "__main__":
    s1 = "bcabc"
    s2 = "cbacdcbc"
    print(Solution().removeDuplicateLetters(s1))
    print(Solution().removeDuplicateLetters(s2))
