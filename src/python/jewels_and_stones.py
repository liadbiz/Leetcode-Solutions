"""
Description:

    You're given strings J representing the types of stones that are jewels,
    and S representing the stones you have.  Each character in S is a type of
    stone you have.  You want to know how many of the stones you have are also
    jewels.

    The letters in J are guaranteed distinct, and all characters in J and S are
    letters. Letters are case sensitive, so "a" is considered a different type
    of stone from "A".

    Example 1:

    Input: J = "aA", S = "aAAbbbb"
    Output: 3
    Example 2:

    Input: J = "z", S = "ZZ"
    Output: 0
    Note:

    S and J will consist of letters and have length at most 50.
    The characters in J are distinct.

Idea:
    use two for loops. In first for loop,iterate each char in string `J`, In
    the second loop, count the times that this char accurs in string `S`, add
    it to the sum. sum is what we want after ieteration.

    function numJewelsInStones1 is the pythonic way. function numJewelsInStones2 
    is the c style.
"""

class Solution:
    def numJewelsInStones1(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        return sum([S.count(i) for i in J])

    def numJewelsInStones2(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        sum = 0
        for i in J:
            for j in S:
                if i == j:
                    sum += 1
        return sum


if __name__ == "__main__":
    J = "aA"
    S = "aAAbbbb"
    print(Solution().numJewelsInStones1(J, S))