"""
description:

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.

Issues:
1. The basic idea is:
    step1: find the min length of all str in the input list strs.
    step2: fix min_index at 0, increase max_index by 1 each iteration, check if the slice 
    [min_index, max_index] of all

In step 2, we can iterate the length from 1 to max_len. We can also iterate the
length from max_len to 1. Obviously, the first one has the greatercomplexity.

2. difference between ' is not ' and ' != ': ' is not ' means the same object,
' != ' means the equal object, so we can not use ' is not ' is 'if' expression
for judging if two prefix from different str are the same.

see https://stackoverflow.com/questions/2209755/python-operation-vs-is-not
for more information

3. ' else ' statement after ' for ' loop means: if the for loop exit normally,
the code in 'else' will be excuted.

"""

class Solution:
    def longestCommonPrefix1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        # handle empty list case
        if not strs:
            return ""
        # if not empty
        # step 1: find the min length of all string in list
        min_len = min([len(s) for s in strs])
        # step2: fix min_index at 0, increase max_index by 1 each iteration, check if the slice 
        # [min_index, max_index] of all
        for i in range(min_len, 0, -1):
            for j in range(len(strs) - 1):
                if strs[j][:i] != strs[j + 1][:i]:
                    break
            else:
            	return strs[0][:i]
        return ""

    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        # handle empty list case
        if not strs:
            return ""
        # if not empty
        # step 1: find the min length of all string in list
        min_len = min([len(s) for s in strs])
        # step2: fix min_index at 0, increase max_index by 1 each iteration, check if the slice 
        # [min_index, max_index] of all
        common_str = ""
        for i in range(1, min_len + 1):
            for j in range(len(strs) - 1):
                if strs[j][:i] != strs[j + 1][:i]:
                    return strs[0][:(i - 1)]
            else:
                common_str = strs[0][:i]
        return common_str

if __name__ == "__main__":
    strs1 = ["flower","flow","flight"]  
    strs2 = ["dog","racecar","car"]  
    # test solution1
    print(Solution().longestCommonPrefix1(strs1))
    print(Solution().longestCommonPrefix1(strs2))
    # test solution2
    print(Solution().longestCommonPrefix2(strs1))
    print(Solution().longestCommonPrefix2(strs2))
