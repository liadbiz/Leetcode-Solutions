class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bin_x = bin(x)[2:]
        bin_y = bin(y)[2:]
        max_len = len(bin_x) if len(bin_x) > len(bin_y) else len(bin_y)
        return [True if bin_x.zfill(max_len)[i] != bin_y.zfill(max_len)[i] else False for i in range(max_len)].count(True)

    
    def hammingDistance2(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return '{:b}'.format(x ^ y).count('1')
      
            
        
if __name__ == "__main__":
    print(Solution().hammingDistance(3, 1))
    print(Solution().hammingDistance2(3, 1))
