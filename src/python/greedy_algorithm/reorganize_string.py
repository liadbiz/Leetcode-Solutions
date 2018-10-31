"""
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].

"""
class Solution:
    # 思路：
    # 思路1: 因为之前做过task
    # scheduler这个题，觉得有些类似的地方，于是按照那个题的思路写的，但是事实
    # 证明这种思路 对于这个题来说过于复杂，因为这个题的的条件相对来说比较宽松
    # 只需要相邻的字符不相同就行了
    # 思路2: 直接将出现次数相对多的放在偶数位置，相对较少的放在奇数位置，然后
    # 不能满足题意的情况是，某一个字符出现的次数过多，即多于半数，那就意味着该
    # 字符至少还占据了最后一个奇数位置，所以只需要检查最后两个字符是否相等即可
    # 这个题很真实的证明了，理解问题的本质才能写出更简洁的代码！
    # 另外关于函数2，有几个细节:
    # a[1::2], a[::2]分别代表奇数和偶数位置
    # a[-1:], a[-2:-1]指的是倒数第一个和倒数第二个元素，而且还避免了a为空的情况
    # str * True => str, str * False => ""
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        import collections
        str_count = collections.Counter(S)
        max_count = max(str_count.values())
        base = "".join(set(i for i in str_count if str_count[i] == max_count))
        filter_dict = {k:v for k, v in str_count.items() if v != max_count}
        other_str = "".join([i * filter_dict[i] for i in filter_dict])
        # print(other_str)
        n = len(other_str)
        if (len(base) == 1 and max_count - 1 <= n) or len(base) > 1:
            res = ""
            for i in range(max_count - 1):
                res += base
                for j in range(n // (max_count - 1) + 1):
                    if j * (max_count - 1) + i < n:
                        # print(other_str[j * (max_count - 1) + i] )
                        res += other_str[j * (max_count - 1) + i]
            return res + base
        return ""

    def reorganizeString2(self, S):
        a = sorted(sorted(S), key=S.count)
        h = len(a) / 2
        a[1::2], a[::2] = a[:h], a[h:]
        return ''.join(a) * (a[-1:] != a[-2:-1])

if __name__ == '__main__':
    S1 = "aab"
    S2 = "aaab"
    S3 = "baaba"
    S4 = "abbabbaaab"
    S5 = "ogccckcwmbmxtsbmozli"
    print(Solution().reorganizeString(S1))
    print(Solution().reorganizeString(S2))
    print(Solution().reorganizeString(S3))
    print(Solution().reorganizeString(S4))
    print(Solution().reorganizeString(S5))
