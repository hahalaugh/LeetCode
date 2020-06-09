class Solution(object):

    def hammingWeightSetRightMost1s(self, n):
        # Set right most 1 to 0
        count = 0
        while n:
            count += 1
            n &= (n - 1)
        return count
    
    def hammingWeightMoveMask(self, n):
        # Move mask in case of signed integer
        count = 0
        mask = 1
        k = n
        while k:
            count += int(bool(n & mask))
            k >>= 1
            mask <<= 1
        return count
    
    def hammingWeightMoveN(self, n):
        # Move n itself. Might process signed negative n incorrectly as left move doesn't change sign bit. 
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            count += n & 1
            n >>= 1
        
        return count
