"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]

"""

class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ""
        i = 0
        while i < len(s):
            d = len(s) - i
            if d >= 2 * k:
                res += s[i:i + k][::-1] + s[ (i + k) : (i + 2 * k) ]
            elif k < d <= 2 * k:
                res += s[i:i + k][::-1] + s[ i + k: ]
            else:
                res += s[i:][::-1]
            i += 2 * k
        return res
       

    def reverseStr2(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l = list(s)
        for i in range(0, len(s), 2 * k):
            l[i:i + k] = reversed(s[i:i + k])
        return ''.join(l)

if __name__ == "__main__":
    s = "abcdefg" 
    print(Solution().reverseStr(s, 2))
    print(Solution().reverseStr2(s, 2))
    
