"""
717.  1-bit and 2-bit Characters

We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:

Input:
bits = [1, 0, 0]

Output: True

Explanation:
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.

Example 2:
Input:

bits = [1, 1, 1, 0]
Output: False

Explanation:
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.

Note:

1 <= len(bits) <= 1000.
bits[i] is always 0 or 1.

Idea:

    + My thought:
        Iterate the `bits`, and check each two element pair, if the the pair equals
        to [1, 1] or [1, 0], increase `index` to `index + 2`, else `index + 1`.
        Stop the iteration if the index reach to `len(bits) - 2` or `len(bits) -
        1`. If the `index` equals to the former, return False, and return True if
        it equals to the latter.
    + Increament pointer:
        When reading from the i-th position, if bits[i] == 0, the next
        character must have 1 bit; else if bits[i] == 1, the next character
        must have 2 bits. We increment our read-pointer i to the start of the
        next character appropriately. At the end, if our pointer is at
        bits.length - 1, then the last character must have a size of 1 bit.
    + Greedy
        The second-last 0 must be the end of a character (or, the beginning of 
        the array if it doesn't exist). Looking from that position forward, the
        array bits takes the form [1, 1, ..., 1, 0] where there are zero or more 
        1's present in total. It is easy to show that the answer is true if and 
        only if there are an even number of ones present.


"""

class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        index = 0
        l = len(bits)
        while index < l - 2:
            b = bits[index: (index + 2)]
            if b == [1, 0] or b == [1, 1]:
                index += 2
            elif b == [0, 1] or b == [0, 0]:
                index += 1
        print(index)
        return False if index == l - 2 else True
    
    def isOneBitCharacter2(self, bits):
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1

    def isOneBitCharacter3(self, bits):
        parity = bits.pop()
        while bits and bits.pop(): parity ^= 1
        return parity == 0

if __name__ == "__main__":
    case1 = [1, 0, 0]
    case2 = [1, 1, 1, 0]
    case3 = [0, 1, 0]
    print(Solution().isOneBitCharacter(case1))
    print(Solution().isOneBitCharacter(case2))
    print(Solution().isOneBitCharacter(case3))
