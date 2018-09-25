"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
Example 3:

Input: ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.

"""

class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        s = {}
        for w in words:
            k = 0
            for c in w:
                k |= 1 << ord(c) - ord('a')
            s[k] = max(s.get(k, 0), len(w))
        return max( [s[i] * s[j] for i in s for j in s if not i & j] or [0] )

    def maxProduct2(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        import itertools
        com = itertools.combinations(words, 2)
        res = []
        for c in com:
            i = list(c)[0]
            j = list(c)[1]
            if not set(i) & set(j):
               res.append(len(i) * len(j))
        return max(res) if res else 0
    
if __name__ == "__main__":
    import timeit
    words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    words2 = ["a","ab","abc","d","cd","bcd","abcd"]
    words3 = ["a","aa","aaa","aaaa"]
    start = timeit.default_timer()
    print(Solution().maxProduct(words))
    print(Solution().maxProduct(words2))
    print(Solution().maxProduct(words3))
    end1 = timeit.default_timer()
    print(Solution().maxProduct2(words))
    print(Solution().maxProduct2(words2))
    print(Solution().maxProduct2(words3))
    end2 = timeit.default_timer()
    print((end1 - start)* 1000)
    print((end2 - start) * 1000)
