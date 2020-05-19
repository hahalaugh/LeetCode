class Solution(object):

    def monotoneIncreasingDigits(self, n):
        """
        :type N: int
        :rtype: int
        """

        def isMonotone(num):
            num = str(num)
            for i in range(len(num) - 1):
                if num[i] > num[i + 1]:
                    return i
            return -1
        
        i = isMonotone(n)
        if i == -1: 
            return n
        else:
            n = str(n)
            result = int(str(int(n[:i + 1]) - 1) + '9' * (len(n) - i - 1))
            return result if isMonotone(result) == -1 else self.monotoneIncreasingDigits(result)


s = Solution()
#print(s.monotoneIncreasingDigits(322))
#print(s.monotoneIncreasingDigits(14))
#print(s.monotoneIncreasingDigits(41))
#print(s.monotoneIncreasingDigits(120))
#print(s.monotoneIncreasingDigits(332))
print(s.monotoneIncreasingDigits(999998))
