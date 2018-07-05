"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
input: haystack = "hello", needle = "ll"

Example 2:
input: haystack = "aaaaa", needle = "bba"

what have learned:
1. first method, we can use str.find() function to return the index of substring in a string, but it's only for python.
2. second method, we can search substring in string, which is O(mn), where m is the length of string, and n is the 
length of substring.
"""

class Solution:
    # first method
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """        
        return haystack.find(needle, 0)
        
    # second method
    def strStr2(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        index = 0
        
        if needle == "":
            return 0
        if needle in haystack:
            c = needle[0]
            for ch in haystack:
                if ch == c:
                    if haystack[index:index+len(needle)] == needle:
                        return index

                index += 1
        return -1

