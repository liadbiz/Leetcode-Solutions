"""
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
"""
class Solution:
    # 思路：
    # 先遍历一遍S，收集其最后出现的位置，第二次遍历的时候，维护两个指针start,
    # end表示当前group的范围，每次遍历更新end的值，当当前遍历值的最后出现位置等于
    # 目前的end时，表示一个group已经划分完毕，更新start值。
    # 第一次自己写的答案
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # gather lowest and highest index of each letter in string S
        index_info = dict()
        for index, s in enumerate(S):
            index_info[s] = index
        # partition proccess
        start, end = 0, 0
        res = []
        while end < len(S) - 1:
            i = start
            end = index_info[S[i]]
            while i < end:
                i += 1
                end = max(index_info[S[i], end])
            res.append(end - start + 1)
            start = i + 1
        return res
    # 改进版
    def partitionLabels2(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        lookup = {s:i for i, s in enumerate(S)}
        start, end = 0, 0
        res = []
        for i, s in enumerate(S):
            end =  max(lookup[s], end)
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res

if __name__ == "__main__":
    S = "ababcbacadefegdehijhklij"
    print(Solution().partitionLabels(S))
    print(Solution().partitionLabels2(S))

