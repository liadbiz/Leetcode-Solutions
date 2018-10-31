"""
Given two arrays A and B of equal size, the advantage of A with respect to B is
the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.


Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]

Note:

1 <= A.length = B.length <= 10000
0 <= A[i] <= 10^9
0 <= B[i] <= 10^9
"""
class Solution:
    # 思路：田忌赛马的思想，找到每个B中的元素对应的最接近的比他大的数，如果没有
    # 就在被挑剩下的A的元素中比其小的
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        import collections
        A = sorted(A)
        lookup = collections.defaultdict(list)
        for i in sorted(B)[::-1]:
            if i < A[-1]:
                lookup[i].append(A.pop())
        return [(lookup[i] or A).pop() for i in B]

if __name__ == '__main__':
    A1 = [2,7,11,15]
    B1 = [1,10,4,11]
    A2 = [12,24,8,32]
    B2 = [13,25,32,11]
    print(Solution().advantageCount(A1, B1))
    print(Solution().advantageCount(A2, B2))
