import math


class Solution(object):

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result = ''
        a = [_ for _ in range(1, n + 1)]
        while k > 0 and a:
            f = math.factorial(len(a) - 1)
            d = int(math.ceil(k / float(f)))
            k -= (d - 1) * f
            result += str(a[d - 1])
            a.pop(d - 1)
        return result

            
s = Solution()
print(s.getPermutation(3, 4))
print(s.getPermutation(4, 9))
