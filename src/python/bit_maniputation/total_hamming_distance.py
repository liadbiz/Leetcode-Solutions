"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:
Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
Note:
Elements of the given array are in the range of 0 to 10^9
Length of the array will not exceed 10^4.


"""

class Solution(object):
    # time exceeded
    # complexity is too O(n^2)
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def HammingDistance(m, n):
            return bin(m ^ n).count('1')
        import itertools
        com = itertools.combinations(nums, 2)
        return sum(HammingDistance(c1, c2) for (c1, c2) in com)

    # AC solution
    # count each bit separately, for each position, if there are two bits are
    # different, the sum distance + 1
    # complexity is just O(n)
    def totalHammingDistance2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(b.count('1') * b.count('0') for b in zip(*map('{:032b}'.format, nums)))



if __name__ == "__main__":
    nums = [4, 14, 2]
    print(Solution().totalHammingDistance(nums))
    print(Solution().totalHammingDistance2(nums))
