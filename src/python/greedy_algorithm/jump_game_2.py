"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
"""
class Solution:
    # 思路1: 时间复杂度为O(n)，空间复杂度为O(n)
    # 第一步：求出每一个点能跳到的最远的地方
    # 第二步：求出能到达每一个点的最小的坐标
    # 第三步：从最后一个点出发，依次原则能到达该点的最小的点为jump经过的点。
    # 可以证明此贪心过程为最优。
    # 实际上还是保留了很多没有用的信息，显然比第二个方法编程要复杂一些。
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) - 1
        reachs = [i + nums[i] for i in range(n)]
        min_reach_index = [float('inf')] * (n + 1)
        m = 0
        for i,r in enumerate(reachs):
            min_reach_index[m:r + 1] = [min(i, _) for _ in
                    min_reach_index[m:r + 1]]
            if r == n:
                break
            m = r + 1
        res = 0
        while n != 0:
            n = min_reach_index[n]
            res += 1
        return res

    # 思路2: 时间复杂度为o(n)，空间复杂度为O(1)
    # 遍历nums，维护变量max_index表示当前遍历过的点能跨到的最远的地方，变量
    # crt_max_index表示我现在所在的点能跳到的最远的地方，当i大于crt_max_index的时候
    # 说明我不能一次就跳到i，所以我要作出一次jump的选择，很明显，应该跳到max_index
    # 对应的那个位置，但是这个位置并不重要，我们只需要将次数加一即可，然后更新
    # crt_max_index为max_index即可。
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        max_index = 0
        crt_max_index = 0
        for i, l in enumerate(nums):
            if i > crt_max_index:
                crt_max_index = max_index
                res += 1
            max_index = max(max_index, i + l)
        return res

if __name__ == "__main__":
    nums1 = [2,3,1,1,4]
    nums2 = [2, 0, 2, 0, 1]
    nums3 = [1, 1, 1, 1]
    nums4 = list(range(1, 25001))[::-1] + [1, 0]
    print(Solution().jump(nums1))
    print(Solution().jump(nums2))
    print(Solution().jump(nums3))
    print(Solution().jump(nums4))
