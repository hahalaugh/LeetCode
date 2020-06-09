class Solution(object):

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xffffffff
        nMask = 0x10000000

        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
            print(bin(a), bin(b))
        return a if a&nMask == 0 else ~(a ^ mask)


s = Solution()
print(s.getSum(-1, 1))
print(s.getSum(-6,3))
