"""
You are given an integer array sorted in ascending order (may contain
duplicates), you need to split them into several subsequences, where each
subsequences consist of at least 3 consecutive integers. Return whether you can
make such a split.

Example 1:
Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5
Example 2:
Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5
Example 3:
Input: [1,2,3,4,4,5]
Output: False
Note:
The length of the input is in range of [1, 10000]
"""
class Solution:
    # 思路：第一个函数是我一开始的想法，遍历nums中的元素，然后如果不能添加到之前
    # 出现的连续序列的话，就算作是重新调整开始一个连续序列，如果能的话，添加到
    # 最近的一个序列(长度最短)，但是复杂度比较高，所以不能AC（超时）
    def isPossible1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import collections
        dq = collections.deque()
        for n in nums:
            for i in reversed(dq):
                if i[1] == n - 1:
                    i[1] += 1
                    break
            else:
                dq.append([n, n])
        print(dq)
        return all(True if p[1] - p[0] >= 2 else False for p in dq )


    # 这个方法复杂度就小很多，O(n)。
    # 因为其实保留具体的连续子序列的信息是没有必要的，上一个函数之所以会超时，
    # 就是因为保留了无用信息。而该方法很好的解决了这个问题
    # 来自: https://leetcode.com/problems/split-array-into-consecutive-
    # subsequences/discuss/106514/Python-esay-understand-solution
    def isPossible2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import collections
        left = collections.Counter(nums)
        end = collections.Counter()
        for i in nums:
            if not left[i]: continue
            left[i] -= 1
            if end[i - 1] > 0:
                end[i - 1] -= 1
                end[i] += 1
            elif left[i + 1] and left[i + 2]:
                left[i + 1] -= 1
                left[i + 2] -= 1
                end[i + 2] += 1
            else:
                return False
        return True

if __name__ == '__main__':
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1,2,3,3,4,4,5,5]
    nums3 = [1,2,3,4,4,5]
    print(Solution().isPossible(nums1))
    print(Solution().isPossible(nums2))
    print(Solution().isPossible(nums3))
