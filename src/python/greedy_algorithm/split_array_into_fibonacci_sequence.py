"""
Given a string S of digits, such as S = "123456579", we can split it into a
Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such
that:

0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type)
F.length >= 3;
and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces, each piece must not have
extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be
done.

Example 1:

Input: "123456579"
Output: [123,456,579]
Example 2:

Input: "11235813"
Output: [1,1,2,3,5,8,13]
Example 3:

Input: "112358130"
Output: []
Explanation: The task is impossible.
Example 4:

Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
Example 5:

Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.
Note:

1 <= S.length <= 200
S contains only digits.

"""
class Solution:
    # 思路：
    # 一个斐波那契数列由最开始的两个数决定，因此我们只需要遍历可能存在的前两个数的组
    # 合，然后判断由此生成的斐波那契数列是否能和S一致，思路比较简单，但是代码写起来
    # 比较复杂，很多小细节
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        def buildFibo(m, n, S):
            if m != '0' and m.startswith('0'):
                return []
            l = len(m)
            m, n = int(m), int(n)
            fibo = [m]
            while l < len(S):
                if S[l: l + len(str(n))] != str(n) or n > 2 ** 31 - 1:
                    return []
                fibo.append(n)
                l += len(str(n))
                m, n = n, m + n
            return [] if l != len(S) else fibo
        n = len(S)
        for i in range(1, n):
            for j in range(1, n - i):
                if i + j <= n -  max(i, j):
                    tmp = buildFibo(S[:i], S[i:i + j], S)
                    if tmp: return tmp
        else:
            return []


if __name__ == '__main__':
    S1 = "123456579"
    S2 = "11235813"
    S3 = "112358130"
    S4 = "0123"
    S5 = "1101111"
    S6 = "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
    print(Solution().splitIntoFibonacci(S1))
    print(Solution().splitIntoFibonacci(S2))
    print(Solution().splitIntoFibonacci(S3))
    print(Solution().splitIntoFibonacci(S4))
    print(Solution().splitIntoFibonacci(S5))
    print(Solution().splitIntoFibonacci(S6))
