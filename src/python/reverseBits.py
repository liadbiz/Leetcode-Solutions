"""
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), 
return 964176192 (represented in binary as 00111001011110000010100101000000).

what have learned:

1. format() function, can be used to convert int number to any other format.
2. int() function, can be used to convert other format number to integer.

"""
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bits = '{0:032b}'.format(n)
        bits_ = bits[::-1]
        return int(bits_, 2)