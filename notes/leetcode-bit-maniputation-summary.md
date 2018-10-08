---
title: Leetcode 位操作问题总结
date: 2018-08-30 19:06:21
tags: leetcode
keywords: leetcode bit maniputation
description: 位操作基础和 Leetcode 上关于位操作的问题示例
---

### 基础

位操作通常用来解决比较底层的计算机问题，比如网络传输，数据压缩，加密有，优化等。
在 [leetcode](https:leetcode.com) 也有 31 道题考察这个知识点。这篇文章主要总结了位
操作的基础知识以及部分题目示例。


常说的位操作符指的是`&`（与），`|`（或）， `^`（亦或）, `~`（否）, 以及`<<`,
`>>`位移运算符。在用位操作来解决问题的时候，选择使用哪个位操作符是关键。下面来看他们的用处。

#### `^` 按位亦或

不同位置 1，相同位置 0。

我们先来看一个简单的题 [461](https://leetcode.com/problems/hamming-distance/description/)。汉明距离我们都很熟悉，如果对应位不同的话就算距离加一，这正好和亦或的逻辑是一样的，因此很容易想到最简单的 AC 解：

```python
class Solution(object):
    def hammingDistance(self, x, y):
        return '{:b}'.format(x ^ y).count('1')

```

题 [477](https://leetcode.com/problems/total-hamming-distance/description/) 是上一题的一种拓展，要求计算列表哪所有组合的汉明距离之和，除了常规的找出所有排列然后计算汉明距离之外，还有另外一种思路：

```python
class Solution:
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(i.count('1') * i.count('0') for i in zip(*map(':032b'.format, nums)))
```

再比如题 [371](https://leetcode.com/problems/sum-of-two-integers/description/) 求两个正数的和，如果不能用求和运算符以及内置的函数的话，只能用位操作
来模拟加法的过程：

```python
class Solution(object):
    def getSum(self, a, b):
        return a if b == 0 else self.getSum(a^b, (a&b)<<1)
```

其中`a^b`表示不考虑进位时两个数相加，而`(a&b)<<1`表示各个位上的进位，两者相加
即可，大家可以用八位表示的两个数相加演示这个过程。由于 python 整形溢出之后会自动转换成长整型，所以对于上述代码对于有溢出情况的加法无法得出正确答案。这里提供一个 AC 解：

```python
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 位能表示的最大整数 (2147483647)
        MAX = 0x7FFFFFFF
        # 32 位能表示的最小负数 (-2147483648)
        MIN = 0x80000000
        # 用来获取最低 32 位的掩码，此题的测试用力应该都是 32 位整数
        # mask = 0xFFFFFFFF
        while b:
            # 只取 32 位保证循环可以结束
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
            #
        return a if a <= MAX else ~(a ^ mask)
```

实际上上述代码还是有问题的，具体什么问题大家可以想一下，因为我也不知道怎么解决，所以这里就不讨论了哈哈哈。

[268](https://leetcode.com/problems/missing-number/) 题也可以用按位亦或的方法解决，当然，你也可以用普通数学方法。

这里利用的是两个相同的数进行按位亦或的操作就会得到 0 这个性质，我们可以把输入数组中的数看成数组下标的乱序排列，因此将数组下标和数做亦或操作，最后结果就是我们要的 missing number。AC 解如下：

```python
class Solution(object):
    def missingNumber(self, nums):
        res = 0
        for i in range(len(nums)):
            res ^= i
            res ^= nums[i]
        res ^= len(nums)
        return res
```

还可以用亦或解决的题有 [476](https://leetcode.com/problems/number-complement/description/)，[693](https://leetcode.com/problems/binary-number-with-alternating-bits/description/)，[389](https://leetcode.com/problems/find-the-difference/description/)，[421](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/) 这里就不一一解释了，感兴趣的可以在我的 [github](https://github.com/liadbiz/leetcode_solutions) 看一下 AC 解。

####  `|` 按位或

有 1 就置 1，全 0 就置 0.

找出小于 n 的最大的 2 的倍数，用位运算也可以解决：

```python
class Solution(object):
    def largest_opwer(self, n):
        n = n | n >> 1
        print(n)
        n = n | n >> 2
        print(n)
        n = n | n >> 4
        print(n)
        n = n | n >> 8
        print(n)
        n = n | n >> 16
        print(n)
        return (n + 1) >> 1
```
如果给定的数大与`2**16`, 那么再向右位移对应的位数即可，主要的思路是使得最高为 1 的位右边的位全部变成 1，然后加一右移一位就是

#### `&` 按位与

全 1 置 1，有 0 置 0。

先来看一下相对简单的题 [338](https://leetcode.com/problems/counting-bits/description/)。这个题是要统计给定`num`范围内所有数的 1 的个数，很容易能想到的解法是遍历所有的数并且分别统计其二进制中 1 的个数，复杂度是`O(n*sizeof(integer))`，但是题中已经说明要求找出`O(n)`的解法。

仔细观察可以看出来，对于每一个偶数 i，其 1 的个数和`i >> 1`是一样的，而对于每一个奇数 i，其 1 的个数是`i >> 2`的 1 的个数加一，按照这个逻辑，就能写出下面的 AC 解：


```python
class Solution(object):
    def countBits2(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0 for i in range(num + 1)]
        for i in range(1, num + 1):
            res[i] = res[i >> 1] + (1 & i)
        return res
```

代码中用`1 & i`判断 i 是偶数还是奇数。

题 [231](https://leetcode.com/problems/power-of-two/description/) 和 [342](https://leetcode.com/problems/power-of-four/description/) 则是用`n&(n-1)`来判断`n`是否是 2 的倍数。
题 [191](https://leetcode.com/problems/number-of-1-bits/description/) 进一步使用该技巧来统计一个二进制数中 1 的个数。

#### `~` 按位取反

1 置 0，0 置 1.

暂时没有做到用这个技巧的题。

#### `>>`右移和`<<`左移

这两个运算符其实基本上在每个位操作的题都会涉及到，用来计算除 2 和乘 2。这里就拿一个比较有意思的题来举例。题号是 [762](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/)。

题目的意思是很清楚的的，也很容易想出一个可行的思路：遍历所给区间的所有数，然后找出其二进制中 1 的个数，判断其是否是素数。但是这样的解法每次在判断某个数为素数的操作上重复了很多次，如果能用位操作优化这个过程就可以降低整个算法的复杂度。

这里直接给出代码：

```python
class Solution:
    def countPrimeSetBits(self, L, R):
        return sum(665772 >> bin(i).count('1') & 1 for i in range(L, R + 1))
```

代码的巧妙之处是利用了题目给的关于`L`和`R`的范围在`10^6`之内，那么很容易知道这之间的数的二进制中 1 的个数最多只能有 19 个，也就是说，我们只需要在判断素数的时候检查其是不是在比 19 小的素数的集合里，也就是是否在`[2, 3, 5, 7, 11, 13,17, 19]`之内。将对应位置 1 其余位置 0，得到 665772，所以在判断是否为素数的时候，只需要将 665772 右移相应的位然后判断最低位是否位 1 即可。

还有一个可以用类似思想解决的题 [78](https://leetcode.com/problems/subsets/description/)，题目要求是求出给定集合的所有子集，根据学过的集合知识可以知道，对于有`n`个元素的集合， 一共有`2**n`个子集，因此我们可以用一个`n`位的计数器来，每一个子集都对应着一个计数器的值，计数器相应位取`1`就代表对应元素在该子集内。对应的 python 的 AC 解如下：

```python

def subsets3(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    n = 1 << len(nums)
    for i in range(n):
        tmp = []
        for j in range(len(nums)):
            if i & (1 << j):
                tmp.append(nums[j])
        res.append(tmp)
    return res
```

题 [201](https://leetcode.com/problems/bitwise-and-of-numbers-range/description/) 也是使用右移的一个例子。

### 总结

从上面的部分示例中可以看出，位运算通常用来降低包含排列，计数等复杂度比较高的操作，当然也可以用来代替乘 2 除 2，判断素数，偶数，倍数等基本操作，但是我认为其意义在于前者，即用计数器来降低设计到排列或者计数的问题的复杂度。

### 参考

https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary:-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently

