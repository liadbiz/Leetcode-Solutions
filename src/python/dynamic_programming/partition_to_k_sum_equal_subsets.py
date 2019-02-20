"""
Given an array of integers nums and a positive integer k, find whether it's
possible to divide this array into k non-empty subsets whose sums are all
equal.

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3),
(2,3) with equal sums.

"""
class Solution:
    # direct search
    # complexity: O(n!)
    # space: O(n)
    # use test case [8, 4, 3, 3, 3, 3, 2, 2, 2, 2], k = 4 for false case
    def canPartitionKSubsets(self, nums: 'List[int]', k: 'int') -> 'bool':
        # each subsets should sum to subsum
        subsum, remainder = divmod(sum(nums), k)
        if remainder or max(nums) > subsum:
            return False

        def search(groups):
            if not nums: return True
            v = nums.pop()
            for i, g in enumerate(groups):
                if g + v <= subsum:
                    groups[i] += v
                    if search(groups): return True
                    groups[i] -= v
                if not g: break
            nums.append(v)
            return False 
        
        # remove the element in nums that equals to subset sum, just a trick to 
        # reduce time
        nums.sort()
        if nums[-1] > subsum: return False
        while nums and nums[-1] == subsum:
            k -= 1
            nums.pop()
        return search([0] * k)

    # dp method
    def canPartitionKSubsets2(self, nums: 'List[int]', k: 'int') -> 'bool':
        subsum, remainder = divmod(sum(nums), k)
        if remainder or max(nums) > subsum:
            return False
        mem = [None] * (1 << len(nums))
        mem[-1] = True
        def search(used, remain):
            if mem[used] is None:
                tar = (remain - 1) % subsum + 1
                mem[used] = any(search(used | (1 << i), remain - n) for i, n in
                        enumerate(nums) if (used >> i) & 1 == 0 and n <= tar)
            return mem[used]
        return search(0, subsum * k)


if __name__ == "__main__":
    nums = [4, 3, 2, 4, 4, 2, 1]
    nums2 = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    # test backtracking method
    print(Solution().canPartitionKSubsets(nums, k))
    print(Solution().canPartitionKSubsets(nums2, k))
    # test dp method
    nums = [4, 3, 2, 4, 4, 2, 1]
    nums2 = [4, 3, 2, 3, 5, 2, 1]
    print(Solution().canPartitionKSubsets2(nums, k))
    print(Solution().canPartitionKSubsets2(nums2, k))
